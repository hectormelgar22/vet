/* ============================================================================
   Equipo · tarjetas 3D
   Hover en escritorio, toque en móvil, teclado accesible; se cierran entre sí
   y respetan prefers-reduced-motion.

   El giro no es plano: la tarjeta se ELEVA hacia el espectador a mitad de
   camino y vuelve a asentarse, con la sombra creciendo a la vez. Sin ese arco
   un flip de 180° se lee como un naipe de cartón; con él, como un objeto con
   grosor. Además la tarjeta se inclina siguiendo al cursor.
   ========================================================================== */
(function () {
  'use strict';

  var cards = Array.prototype.slice.call(document.querySelectorAll('.flip-card'));
  if (!cards.length) return;

  document.documentElement.classList.add('has-js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isFine = window.matchMedia('(pointer: fine)').matches;
  var hasGSAP = typeof window.gsap !== 'undefined';

  /* Cierra las hermanas del grupo. Recibe quién las cierra para no depender de
     qué motor de animación esté disponible. */
  function closeSiblings(card, close) {
    var group = card.closest('[data-flip-group]');
    if (!group) return;
    group.querySelectorAll('.flip-card.flipped').forEach(function (s) {
      if (s !== card) close(s);
    });
  }

  /* ---- Sin GSAP: el CSS ya gira con la clase, solo falta alternarla ------ */
  if (!hasGSAP) {
    var closePlain = function (c) {
      c.classList.remove('flipped');
      c.setAttribute('aria-pressed', 'false');
    };
    cards.forEach(function (card) {
      card.addEventListener('click', function () {
        var open = !card.classList.contains('flipped');
        if (open) closeSiblings(card, closePlain);
        card.classList.toggle('flipped', open);
        card.setAttribute('aria-pressed', String(open));
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') cards.forEach(closePlain);
    });
    return;
  }

  var gsap = window.gsap;
  if (window.ScrollTrigger) gsap.registerPlugin(window.ScrollTrigger);

  var FLIP_DUR = 0.82;

  function setFlipped(card, open) {
    if (card.classList.contains('flipped') === open) return;
    if (open) closeSiblings(card, function (c) { setFlipped(c, false); });
    card.classList.toggle('flipped', open);
    card.setAttribute('aria-pressed', String(open));

    var tilt = card.querySelector('.flip-card__tilt');
    var inner = card.querySelector('.flip-card__inner');
    var edge = card.querySelector('.flip-card__edge');
    var shadow = card.querySelector('.flip-card__shadow');
    var back = card.querySelector('.flip-card__back');
    var backBits = back ? back.children : [];
    var dur = reduceMotion ? 0 : FLIP_DUR;

    gsap.killTweensOf([inner, shadow, edge]);
    gsap.killTweensOf(backBits);

    var tl = gsap.timeline();

    /* El giro. */
    tl.to(inner, { rotateY: open ? 180 : 0, duration: dur, ease: 'power3.inOut' }, 0);

    if (!reduceMotion) {
      /* El arco de elevación: sube en la primera mitad, baja en la segunda. */
      tl.to(tilt, { z: 90, duration: dur * 0.5, ease: 'power2.out' }, 0)
        .to(tilt, { z: 0, duration: dur * 0.5, ease: 'power2.in' }, dur * 0.5);

      /* La sombra acompaña: se separa y difumina mientras está en el aire. */
      tl.to(shadow, {
        opacity: 0.5, scale: 1.1, y: 16,
        duration: dur * 0.5, ease: 'power2.out'
      }, 0)
        .to(shadow, {
          opacity: 0.3, scale: 1, y: 0,
          duration: dur * 0.5, ease: 'power2.in'
        }, dur * 0.5);

      /* El canto se asoma por el lado contrario según hacia dónde gira. */
      tl.to(edge, {
        opacity: open ? 0.65 : 0.25, x: open ? -4 : 4,
        duration: dur * 0.7, ease: 'power3.inOut'
      }, 0);

      /* El reverso se compone después de cruzar los 90°, cuando ya se ve. */
      if (open && backBits.length) {
        tl.fromTo(backBits,
          { autoAlpha: 0, y: 16 },
          { autoAlpha: 1, y: 0, duration: 0.45, stagger: 0.07, ease: 'power3.out' },
          dur * 0.58);
      } else if (backBits.length) {
        tl.set(backBits, { autoAlpha: 1, y: 0 }, dur);
      }
    }
  }

  /* ---- Inclinación siguiendo al cursor ---------------------------------- */
  /* Va en .flip-card__tilt, no en .flip-card__inner: si compartieran elemento,
     el giro de 180° y la inclinación se sobrescribirían mutuamente. */
  function bindTilt(card) {
    var tilt = card.querySelector('.flip-card__tilt');
    if (!tilt) return;
    var MAX = 7;
    var raf = null, px = 0, py = 0;

    function apply() {
      raf = null;
      var r = card.getBoundingClientRect();
      var nx = (px - r.left) / r.width - 0.5;
      var ny = (py - r.top) / r.height - 0.5;
      gsap.to(tilt, {
        rotationY: nx * MAX * 2,
        rotationX: -ny * MAX * 2,
        duration: 0.5,
        ease: 'power2.out',
        overwrite: 'auto'
      });
    }

    card.addEventListener('pointermove', function (e) {
      if (e.pointerType !== 'mouse') return;
      px = e.clientX; py = e.clientY;
      if (!raf) raf = requestAnimationFrame(apply);
    });
    card.addEventListener('pointerleave', function () {
      if (raf) { cancelAnimationFrame(raf); raf = null; }
      gsap.to(tilt, { rotationX: 0, rotationY: 0, duration: 0.6, ease: 'power3.out', overwrite: 'auto' });
    });
  }

  cards.forEach(function (card) {
    function enter() { setFlipped(card, true); }
    function leave() {
      if (!card.matches(':hover') && document.activeElement !== card) setFlipped(card, false);
    }
    card.addEventListener('click', function () {
      if (!isFine || reduceMotion) setFlipped(card, !card.classList.contains('flipped'));
    });
    if (isFine && !reduceMotion) {
      card.addEventListener('mouseenter', enter);
      card.addEventListener('mouseleave', leave);
      card.addEventListener('focus', enter);
      card.addEventListener('blur', leave);
      bindTilt(card);
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') cards.forEach(function (c) { setFlipped(c, false); });
  });

  /* ---- Entrada al llegar a la sección ------------------------------------ */
  /* Las tarjetas llegan girando levemente sobre su eje X, como si se posaran:
     insinúa que son objetos con volumen antes incluso de tocarlas. */
  if (window.ScrollTrigger && !reduceMotion) {
    var grid = document.querySelector('.team-flip__grid');
    if (grid) {
      gsap.from(cards, {
        y: 46, rotationX: -12, autoAlpha: 0, transformOrigin: 'center bottom',
        duration: 0.85, ease: 'power3.out', stagger: 0.1,
        scrollTrigger: { trigger: grid, start: 'top 86%', once: true }
      });
    }
  }
})();
