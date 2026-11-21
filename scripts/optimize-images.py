#!/usr/bin/env python3
"""Erzeugt die ausgelieferten Bild-Assets der Website aus den Quelldateien.

Quellen liegen bewusst NICHT im Repo (GitHub Pages liefert alles aus, was drin liegt):
  icon   -> das 1024er App-Icon (RGBA, transparent). Original: `git show 40c80f8:caltracker_icon.png`
  phones -> Ordner mit iPhone-Mockups `phone-<name>.png` (transparent, ~1000 px breit),
            erzeugt aus den Rohaufnahmen mit scripts/store_screenshots/ im App-Repo.

Aufruf (Pillow genuegt, kein cwebp/ImageMagick noetig):
  python scripts/optimize-images.py icon   <icon-1024.png>
  python scripts/optimize-images.py phones <ordner> [--hero]   # --hero erzeugt zusaetzlich hero-phone-*.webp (Faecher)
"""
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "img"

PHONES = {                       # Name -> Breiten (CSS-Slot x DPR)
    "home": (390, 780),
    "scan": (390, 780),
    "activity": (390, 780),
    "eval": (390, 780),
    "history": (390, 780),
    "weight": (390, 780),
}
HERO = {"home": 640, "scan": 640, "activity": 640}   # Faecher oben: eigene Dateien hero-phone-*.webp


def clean_alpha(im):
    """Unsichtbare Pixel auf RGB 0 setzen: Rauschen unter alpha=0 blaeht das PNG sonst um das 20-Fache auf."""
    px = im.load()
    r, g, b, a = im.split()
    zero = a.point(lambda v: 255 if v == 0 else 0)
    black = Image.new("L", im.size, 0)
    for ch in (r, g, b):
        ch.paste(black, mask=zero)
    return Image.merge("RGBA", (r, g, b, a))


def resize(im, w):
    return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)


def palette(im):
    """256-Farben-PNG (inkl. Alpha): das weiche Icon-Glimmen bleibt sauber, Datei ~85 % kleiner."""
    return im.quantize(256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)


def icon(src):
    master = clean_alpha(Image.open(src).convert("RGBA"))
    IMG.mkdir(exist_ok=True)
    palette(resize(master, 512)).save(ROOT / "caltracker_icon.png", optimize=True)   # Dateiname bleibt (invite/, og:image-Caches, Legacy-Verweise)
    palette(resize(master, 192)).save(IMG / "icon-192.png", optimize=True)           # Favicon (Google will Vielfache von 48)
    white = Image.new("RGBA", (180, 180), (255, 255, 255, 255))                      # apple-touch-icon darf nicht transparent sein
    white.alpha_composite(resize(master, 180))
    white.convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(IMG / "icon-180.png", optimize=True)
    resize(master, 96).save(IMG / "icon-96.webp", quality=90, method=6)     # Logo in Header/Footer (36 px @2x/3x)
    for p in [ROOT / "caltracker_icon.png", *sorted(IMG.glob("icon-*"))]:
        print(f"{p.relative_to(ROOT)}  {p.stat().st_size / 1024:.1f} KB")


def phones(folder, hero=False):
    folder = Path(folder)
    IMG.mkdir(exist_ok=True)
    for name, widths in PHONES.items():
        im = Image.open(folder / f"phone-{name}.png").convert("RGBA")
        for w in widths:
            out = IMG / f"phone-{name}-{w}.webp"
            resize(im, w).save(out, quality=82, method=6, alpha_quality=90)
            print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.1f} KB")
    for name, w in (HERO.items() if hero else ()):
        out = ROOT / f"hero-phone-{'progress' if name == 'activity' else name}.webp"
        resize(Image.open(folder / f"phone-{name}.png").convert("RGBA"), w).save(out, quality=82, method=6, alpha_quality=90)
        print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--hero"]
    if len(args) != 2 or args[0] not in ("icon", "phones"):
        sys.exit(__doc__)
    if args[0] == "icon":
        icon(args[1])
    else:
        phones(args[1], hero="--hero" in sys.argv)
