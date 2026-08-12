/* ============================================================================
   Gestión de consentimiento · Google Consent Mode v2
   ----------------------------------------------------------------------------
   - Por defecto todo denegado (declarado en el <head>, antes de cualquier tag).
   - El banner ofrece "Rechazar todo" y "Aceptar todo" con idéntica prominencia.
   - La decisión se guarda con versión y fecha para poder renovarla (la AEPD
     recomienda revalidar el consentimiento como máximo cada 24 meses).
   ========================================================================== */
(function () {
  'use strict';

  var STORE_KEY = 'vc_consent_v2';
  var MAX_AGE_DAYS = 180;

  var banner = document.getElementById('cookie-banner');
  var btnAccept = document.getElementById('cookie-accept');
  var btnReject = document.getElementById('cookie-reject');
  if (!banner || !btnAccept || !btnReject) return;

  var lastFocused = null;

  function readDecision() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      if (!raw) return null;
      var saved = JSON.parse(raw);
      var ageDays = (Date.now() - (saved.ts || 0)) / 86400000;
      if (ageDays > MAX_AGE_DAYS) return null;   // caducado: se vuelve a preguntar
      return saved;
    } catch (e) {
      return null;
    }
  }

  function applyConsent(state) {
    if (typeof window.gtag !== 'function') return;
    window.gtag('consent', 'update', {
      ad_storage: state,
      ad_user_data: state,
      ad_personalization: state,
      analytics_storage: state
    });
    window.dataLayer.push({ event: 'consent_decision', consent_state: state });
  }

  function save(state) {
    try {
      localStorage.setItem(STORE_KEY, JSON.stringify({ state: state, ts: Date.now(), v: 2 }));
    } catch (e) { /* modo privado: la decisión vale solo para esta sesión */ }
  }

  function openBanner() {
    lastFocused = document.activeElement;
    banner.hidden = false;
    requestAnimationFrame(function () {
      banner.classList.add('is-visible');
      btnReject.focus({ preventScroll: true });
    });
    document.addEventListener('keydown', onKeydown);
  }

  function closeBanner() {
    banner.classList.remove('is-visible');
    document.removeEventListener('keydown', onKeydown);
    window.setTimeout(function () { banner.hidden = true; }, 300);
    if (lastFocused && typeof lastFocused.focus === 'function') {
      lastFocused.focus({ preventScroll: true });
    }
  }

  /* Esc equivale a rechazar: no se interpreta el silencio como aceptación. */
  function onKeydown(e) {
    if (e.key === 'Escape') decide('denied');
  }

  function decide(state) {
    applyConsent(state);
    save(state);
    closeBanner();
  }

  btnAccept.addEventListener('click', function () { decide('granted'); });
  btnReject.addEventListener('click', function () { decide('denied'); });

  /* Reapertura desde el pie o desde el bloque del mapa. */
  Array.prototype.forEach.call(document.querySelectorAll('.js-open-cookies'), function (el) {
    el.addEventListener('click', openBanner);
  });

  var decision = readDecision();
  if (decision) {
    applyConsent(decision.state);
  } else {
    window.setTimeout(openBanner, 900);
  }
})();
