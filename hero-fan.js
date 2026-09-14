(() => {
  const stage = document.querySelector('[data-fan]');
  if (!stage) return;

  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canHover = matchMedia('(hover: hover)').matches;
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;

  const fanOut = () => {
    stage.classList.add('is-fanned');
    setTimeout(() => stage.classList.add('is-settled'), reduceMotion ? 0 : 1400);
  };

  if (reduceMotion) {
    fanOut();
  } else {
    const io = new IntersectionObserver((entries) => {
      if (entries.some((e) => e.isIntersecting)) {
        io.disconnect();
        setTimeout(fanOut, 250);
      }
    }, { threshold: 0.3 });
    io.observe(stage);
  }

  if (!canHover) {
    stage.addEventListener('click', () => {
      if (stage.classList.contains('is-fanned')) stage.classList.toggle('is-spread');
    });
  }

  if (finePointer && !reduceMotion) {
    const tilt = stage.querySelector('.fan-tilt');
    let frame = 0;
    stage.addEventListener('pointermove', (e) => {
      const rect = stage.getBoundingClientRect();
      const px = (e.clientX - rect.left) / rect.width - 0.5;
      const py = (e.clientY - rect.top) / rect.height - 0.5;
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        tilt.style.setProperty('--tilt-y', (px * 9).toFixed(2) + 'deg');
        tilt.style.setProperty('--tilt-x', (py * -6).toFixed(2) + 'deg');
      });
    });
    stage.addEventListener('pointerleave', () => {
      cancelAnimationFrame(frame);
      tilt.style.setProperty('--tilt-y', '0deg');
      tilt.style.setProperty('--tilt-x', '0deg');
    });
  }
})();
