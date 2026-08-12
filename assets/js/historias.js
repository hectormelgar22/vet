/* ============================================================================
   Historias felices · Perspective Zoom Effect
   Basado en el montaje original (GSAP ScrollSmoother + SplitText), adaptado a
   Vitalis con degradación limpia (sin GSAP / movimiento reducido).
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGSAP = typeof window.gsap !== 'undefined';

  /* ---- Camino sin animación: se muestra el collage como galería estática --- */
  if (reduceMotion || !hasGSAP) {
    root.classList.add('reduce-motion');
    return;
  }

  var gsap = window.gsap;
  var plugins = [];
  if (window.ScrollTrigger) plugins.push(window.ScrollTrigger);
  if (window.ScrollSmoother) plugins.push(window.ScrollSmoother);
  if (window.SplitText) plugins.push(window.SplitText);
  if (plugins.length) gsap.registerPlugin.apply(gsap, plugins);

  if (!window.ScrollTrigger) { root.classList.add('reduce-motion'); return; }

  /* ---- Scroll suave con efectos (necesario para el paralaje del original) -- */
  if (window.ScrollSmoother) {
    window.ScrollSmoother.create({
      smooth: 1,
      effects: true,
      normalizeScroll: true
    });
  }

  /* ---- 1) Collage: cada capa avanza hacia la cámara (eje Z) y se aclara ---- */
  gsap.timeline({
    scrollTrigger: {
      trigger: '.zoom-container',
      start: 'top top',
      end: '+=150%',
      pin: true,
      scrub: 1
    }
  })
    /* Recorrido en Z más corto que el del montaje original: nuestras fotos
       arrancan bastante más grandes, así que con z:800 (≈9× de escala) se
       saldrían de pantalla. Con estos valores crecen ~1,5-2,6× y se aprecian. */
    .to(".zoom-item[data-layer='3']", { opacity: 1, z: 560, ease: 'power1.inOut' }, 0)
    .to(".zoom-item[data-layer='2']", { opacity: 1, z: 440, ease: 'power1.inOut' }, 0)
    .to(".zoom-item[data-layer='1']", { opacity: 1, z: 320, ease: 'power1.inOut' }, 0)
    .to('.heading', { opacity: 1, z: 50, ease: 'power1.inOut' }, 0);

  /* ---- 2) Frase que se revela letra a letra al fijar la sección ----------- */
  var quote = document.querySelector('.opacity-reveal');
  if (quote && window.SplitText) {
    function buildQuoteTimeline(split) {
      gsap.set(split.chars, { opacity: 0.2 });
      gsap.timeline({
        scrollTrigger: {
          trigger: '.section-stick',
          pin: true,
          start: 'center center',
          end: '+=1500',
          scrub: 1
        }
      })
        .to(split.chars, { opacity: 1, duration: 1, ease: 'none', stagger: 1 })
        .to({}, { duration: 10 })
        .to(quote, { opacity: 0, scale: 1.2, duration: 50 });
    }

    /* SplitText 3.13 admite callback onSplit y espera a las fuentes. */
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () {
        buildQuoteTimeline(window.SplitText.create(quote, { type: 'chars' }));
        window.ScrollTrigger.refresh();
      });
    } else {
      buildQuoteTimeline(window.SplitText.create(quote, { type: 'chars' }));
    }
  }

  /* Recalcular medidas cuando cargan imágenes y fuentes. */
  window.addEventListener('load', function () { window.ScrollTrigger.refresh(); });
})();
