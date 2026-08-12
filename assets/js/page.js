/* ============================================================================
   Páginas interiores · solo lo imprescindible
   No carga main.js entero (triaje, hero, collage, formulario…): aquí nada de
   eso existe. Esto se ocupa de la píldora de navegación, el año del pie y el
   desplazamiento suave de los enlaces internos.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --------------------------------------------------------------- Año */
  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  /* ------------------------------------------------------ Menú y píldora */
  var nav = document.getElementById('nav');
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('menu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      toggle.setAttribute('aria-label', open ? 'Abrir menú' : 'Cerrar menú');
      menu.classList.toggle('is-open', !open);
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        menu.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Abrir menú');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) {
        menu.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  var lastY = window.scrollY;
  var navHidden = false;
  var ticking = false;

  function onScroll() {
    if (ticking || !nav) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      var y = window.scrollY;
      nav.classList.toggle('is-stuck', y > 10);
      var menuOpen = menu && menu.classList.contains('is-open');
      if (!reduceMotion && !menuOpen) {
        if (y < 40) navHidden = false;
        else if (y > lastY + 3 && y > 140) navHidden = true;
        else if (y < lastY - 3) navHidden = false;
      } else {
        navHidden = false;
      }
      nav.classList.toggle('is-hidden', navHidden);
      lastY = y;
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ------------------------------- Desplazamiento suave de enlaces internos */
  /* Igual que en la home: se hace desde JS y no con `scroll-behavior: smooth`,
     que interfiere con las mediciones de ScrollTrigger (ver styles.css). */
  document.addEventListener('click', function (e) {
    var link = e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!link) return;
    var id = link.getAttribute('href');
    if (!id || id === '#' || id.length < 2) return;
    var target = document.getElementById(id.slice(1));
    if (!target) return;

    e.preventDefault();
    window.scrollTo({
      top: Math.max(0, target.getBoundingClientRect().top + window.scrollY - 96),
      behavior: reduceMotion ? 'auto' : 'smooth'
    });
    if (history.replaceState) history.replaceState(null, '', id);
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  });
})();
