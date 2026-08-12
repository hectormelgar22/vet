/* ============================================================================
   Experiencia · scroll cinematográfico
   Basado en el montaje original (Lenis + GSAP ScrollTrigger), adaptado a
   Vitalis: vídeos propios, textos en español, degradación y reduce-motion.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var smallScreen = window.matchMedia('(max-width: 768px)').matches;
  var conn = navigator.connection || {};

  /* ---- Carga de vídeos: versión ligera en móvil; respeta el ahorro de datos.
     Los vídeos siempre acaban visibles (autoplay silenciado). ---------------- */
  function loadVideo(v, autoplay) {
    if (!v) return;
    var wantSmall = smallScreen || conn.saveData;
    var src = wantSmall ? v.getAttribute('data-src-sm') : v.getAttribute('data-src-lg');
    if (!src) return;
    v.setAttribute('src', src);
    v.load();
    if (autoplay) {
      var p = v.play();
      if (p && typeof p.catch === 'function') p.catch(function () {});
    }
  }

  var video = document.getElementById('video');
  var footerVideo = document.querySelector('.mountain-footer video');
  loadVideo(video, true);
  loadVideo(footerVideo, reduceMotion); /* en reduce-motion ya está a la vista */

  /* ---- Copiar el correo al pulsar el botón de contacto --------------------- */
  var emailBtn = document.querySelector('.contact-btn');
  var emailElement = document.getElementById('email-copy');
  if (emailBtn && emailElement) {
    var originalText = emailElement.textContent;
    var copyTimeout = null;

    function copyEmail(e) {
      /* No copiar si se ha pulsado el propio enlace "Pedir cita online". */
      if (e && e.target && e.target.closest && e.target.closest('.contact-cta')) return;
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(originalText).then(function () {
        emailElement.textContent = 'correo copiado ✓';
        if (copyTimeout) clearTimeout(copyTimeout);
        copyTimeout = setTimeout(function () { emailElement.textContent = originalText; }, 2000);
      }).catch(function () {});
    }
    emailBtn.addEventListener('click', copyEmail);
    emailBtn.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); copyEmail(e); }
    });
  }

  var hasGSAP = typeof window.gsap !== 'undefined';

  /* ---- Camino sin animación: reduce-motion o sin GSAP --------------------- */
  if (reduceMotion || !hasGSAP) {
    root.classList.add('reduce-motion');
    loadVideo(footerVideo, true);
    return;
  }

  var gsap = window.gsap;
  if (window.ScrollTrigger) gsap.registerPlugin(window.ScrollTrigger);
  if (window.CustomEase) {
    gsap.registerPlugin(window.CustomEase);
    window.CustomEase.create('softReveal', '0.5, 0, 0, 1');
  }

  /* ---- Scroll suave (Lenis), sincronizado con ScrollTrigger --------------- */
  if (typeof window.Lenis !== 'undefined') {
    var lenis = new window.Lenis({
      duration: 0.9,
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      orientation: 'vertical',
      gestureOrientation: 'vertical',
      smoothWheel: true
    });
    if (window.ScrollTrigger) lenis.on('scroll', window.ScrollTrigger.update);
    gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  if (!window.ScrollTrigger) return;

  var videoContainer = document.getElementById('video-container');
  var videoOverlay = document.querySelector('.video-overlay');
  var overlayCaption = document.querySelector('.video-overlay .caption');
  var overlayContent = document.querySelector('.video-overlay .content');
  var mountainFooter = document.querySelector('.mountain-footer');

  /* ---- Cabecera: efecto rollo de película (gira y se desvanece) ----------- */
  var heroTl = gsap.timeline({
    scrollTrigger: {
      trigger: '.container',
      start: 'top top',
      end: 'top+=420 top',
      scrub: 1.2
    }
  });
  gsap.utils.toArray('.header-content > *').forEach(function (element, index) {
    heroTl.to(element, {
      rotationX: 90,
      y: -30,
      scale: 0.7,
      opacity: 0,
      filter: 'blur(4px)',
      ease: 'power3.inOut',
      transformOrigin: 'center top'
    }, index * 0.08);
  });

  /* Capa de oscurecido sobre el vídeo mientras crece. */
  var overlay = document.createElement('div');
  overlay.style.cssText = 'position:absolute;inset:0;background-color:rgba(0,0,0,0);pointer-events:none;z-index:1;';
  videoContainer.appendChild(overlay);

  /* ---- Vídeo central: crece hasta llenar la pantalla + revela el texto ---- */
  var tl = gsap.timeline({
    scrollTrigger: {
      trigger: '.scroll-container',
      start: 'top top',
      end: 'bottom bottom',
      scrub: 1.2,
      onEnter: function () { if (video) video.play().catch(function () {}); }
    }
  });

  tl.to(videoContainer, { width: '92vw', height: '88vh', borderRadius: '0px', ease: 'expo.out', duration: 0.5 }, 0)
    .to(video, { scale: 1.1, ease: 'expo.out', duration: 0.5 }, 0)
    .to(overlay, { backgroundColor: 'rgba(11,33,30,0.42)', ease: 'power3.inOut', duration: 0.5 }, 0)
    .to(videoOverlay, { clipPath: 'inset(0% 0 0 0)', ease: 'expo.out', duration: 0.3 }, 0.4)
    .to(overlayCaption, { y: 0, ease: 'expo.out', duration: 0.3 }, 0.45)
    .to(overlayContent, { filter: 'blur(0px)', scale: 1, ease: 'expo.out', duration: 0.4 }, 0.45)
    .to('.video-overlay h2, .video-overlay p', { y: 0, ease: 'expo.out', duration: 0.4, stagger: 0.05 }, 0.5);

  /* ---- Vídeo de cierre: se revela de abajo arriba ------------------------- */
  gsap.to(mountainFooter, {
    scrollTrigger: {
      trigger: '.footer-content',
      start: 'top 80%',
      end: 'top 40%',
      scrub: 1.2,
      onEnter: function () { if (footerVideo) footerVideo.play().catch(function () {}); }
    },
    clipPath: 'inset(0% 0 0 0)',
    ease: 'expo.out'
  });

  /* Botón de contacto: aparece con el vídeo de cierre. */
  gsap.to('.mountain-footer .contact-btn', {
    scrollTrigger: { trigger: '.mountain-footer', start: 'top 60%', end: 'top 30%', scrub: 0.8 },
    opacity: 1,
    ease: 'expo.out'
  });

  /* Revelado de la cita. */
  gsap.utils.toArray('.footer-content p').forEach(function (text) {
    gsap.from(text, {
      scrollTrigger: { trigger: text, start: 'top 85%', end: 'top 68%', scrub: 1.2 },
      y: 15,
      filter: 'blur(5px)',
      opacity: 0.2,
      ease: 'expo.out'
    });
  });

  /* Recalcular medidas cuando cargan fuentes y vídeos. */
  window.addEventListener('load', function () { window.ScrollTrigger.refresh(); });
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { window.ScrollTrigger.refresh(); });
  }
})();
