# -*- coding: utf-8 -*-
"""Genera las páginas interiores (legales y detalle de servicio).

Todas comparten cabecera, píldora de navegación y pie, de modo que si cambia
la identidad basta con tocar este archivo y volver a ejecutarlo:

    python .build/pagegen.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEL_HREF = "+34910305305"
TEL_TXT = "910 305 305"
MAIL = "citas@vitalisveterinaria.es"
BRAND = "Clínica Veterinaria Vitalis"
SITE = "https://www.vitalisveterinaria.es"

CONSENT = """<!-- ============================================================================
     CONSENT MODE v2 — debe ejecutarse ANTES de cualquier etiqueta de medición.
     Todo denegado por defecto (RGPD / LOPDGDD / AEPD).
     ============================================================================ -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'functionality_storage': 'granted',
    'security_storage': 'granted'
  });
</script>"""

FAVICON = ("<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
           "viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230F3D36'/%3E%3Cpath "
           "d='M4 17h5l2-6 3 12 3-9 2 3h9' fill='none' stroke='%23E4572E' stroke-width='2.2' "
           "stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E\">")

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Figtree:wght@300..800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">"""

ARROW = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 '
         '11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 '
         '.57 3.6 1 1 0 0 1-.25 1z"/></svg>')


def head(title, desc, canonical, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">

{CONSENT}

<script>document.documentElement.classList.add('js');</script>

<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE}/{canonical}">
<meta name="theme-color" content="#FBF9F3">

<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-cover.jpg">

{FAVICON}

{FONTS}
<link rel="stylesheet" href="assets/css/styles.css?v=12">
<link rel="stylesheet" href="assets/css/page.css?v=1">{extra_css}
</head>
"""


NAV = f"""<a class="skip-link" href="#contenido">Saltar al contenido principal</a>

<header class="nav" id="nav">
  <div class="nav__inner">
    <a class="brand" href="index.html" aria-label="{BRAND}, inicio">
      <span class="brand__mark" aria-hidden="true">
        <svg viewBox="0 0 40 40"><path d="M4 21h6.5l2.6-8 3.9 16 3.9-12.5 2.6 4.5H36" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <span class="brand__text">
        <strong>{BRAND}</strong>
        <span>Veterinaria · Madrid</span>
      </span>
    </a>

    <nav class="nav__links" id="menu" aria-label="Navegación principal">
      <a href="index.html#servicios">Servicios</a>
      <a href="index.html#peluqueria">Peluquería</a>
      <a href="index.html#visita">Tu visita</a>
      <a href="index.html#instalaciones">Instalaciones</a>
      <a href="index.html#opiniones">Opiniones</a>
      <a href="index.html#equipo">Equipo</a>
      <a href="index.html#faq">Preguntas</a>
    </nav>

    <div class="nav__actions">
      <a class="nav__call" href="tel:{TEL_HREF}">
        <span class="pulse-dot pulse-dot--live" aria-hidden="true"></span>
        <span class="nav__call-text">
          <span class="nav__call-label">Urgencias 24 h</span>
          <strong>{TEL_TXT}</strong>
        </span>
      </a>
      <a class="btn btn--solid" href="index.html#contacto">Pedir cita</a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="menu" aria-label="Abrir menú">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""


def footer(services):
    svc_links = "\n".join(
        f'      <a href="{s["slug"]}.html">{s["nav"]}</a>' for s in services)
    return f"""<footer class="footer">
  <div class="wrap footer__grid">
    <div class="footer__brand">
      <span class="brand__mark" aria-hidden="true">
        <svg viewBox="0 0 40 40"><path d="M4 21h6.5l2.6-8 3.9 16 3.9-12.5 2.6 4.5H36" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <p class="footer__claim">
        {BRAND}. Medicina, cirugía y hospitalización veterinaria en Madrid,
        con guardia presencial las 24 horas.
      </p>
      <p class="footer__reg">
        Centro veterinario inscrito en el Registro de Centros Veterinarios de la
        Comunidad de Madrid nº RCV-2871. Dirección técnica: Elena Marín, colegiada nº 28345
        del Colegio Oficial de Veterinarios de Madrid.
      </p>
    </div>

    <nav class="footer__col" aria-label="Servicios">
      <h3>Servicios</h3>
{svc_links}
    </nav>

    <nav class="footer__col" aria-label="Herramientas">
      <h3>Herramientas</h3>
      <a href="calendario-mascota.html">Calendario de vacunas</a>
      <a href="consultor-toxicos.html">¿Puede comer esto?</a>
      <a href="calculadora-nutricion.html">Calculadora de ración</a>
    </nav>

    <nav class="footer__col" aria-label="Clínica">
      <h3>Clínica</h3>
      <a href="index.html#visita">Tu visita</a>
      <a href="index.html#peluqueria">Peluquería</a>
      <a href="index.html#instalaciones">Instalaciones</a>
      <a href="index.html#opiniones">Opiniones</a>
      <a href="index.html#equipo">Equipo</a>
      <a href="index.html#faq">Preguntas frecuentes</a>
      <a href="guia-veterinaria-madrid.html">Guía: elegir veterinaria</a>
    </nav>

    <div class="footer__col">
      <h3>Contacto</h3>
      <a href="tel:{TEL_HREF}">{TEL_TXT}</a>
      <a href="mailto:{MAIL}">{MAIL}</a>
      <p class="footer__addr">Calle de Alcalá, 415<br>28027 Madrid</p>
    </div>
  </div>

  <div class="wrap footer__bottom">
    <p>© <span id="year">2026</span> {BRAND}. Todos los derechos reservados.</p>
    <nav class="footer__legal" aria-label="Información legal">
      <a href="aviso-legal.html">Aviso legal</a>
      <a href="privacidad.html">Política de privacidad</a>
      <a href="cookies.html">Política de cookies</a>
      <button class="footer__cookies js-open-cookies" type="button">Preferencias de cookies</button>
    </nav>
  </div>
</footer>
"""


COOKIE_BANNER = f"""<div class="cookie" id="cookie-banner" role="dialog" aria-modal="false"
     aria-labelledby="cookie-title" aria-describedby="cookie-text" hidden>
  <div class="wrap cookie__inner">
    <div>
      <h2 class="cookie__title" id="cookie-title">Cookies</h2>
      <p class="cookie__text" id="cookie-text">
        Usamos cookies propias necesarias para que la web funcione. Las de medición
        solo se activan si las aceptas. Puedes cambiar de idea cuando quieras.
        <a href="cookies.html">Ver la política de cookies</a>.
      </p>
    </div>
    <div class="cookie__actions">
      <button class="btn btn--cookie btn--ghost" type="button" id="cookie-reject">Rechazar todo</button>
      <button class="btn btn--cookie btn--solid" type="button" id="cookie-accept">Aceptar todo</button>
    </div>
  </div>
</div>

<script src="assets/js/cookies.js?v=3" defer></script>
<script src="assets/js/page.js?v=1" defer></script>
</body>
</html>
"""


def breadcrumb(title):
    return f"""      <nav class="breadcrumb" aria-label="Migas de pan">
        <a href="index.html">Inicio</a>
        <span class="breadcrumb__sep" aria-hidden="true">/</span>
        <span aria-current="page">{title}</span>
      </nav>"""


def page_cta(title, text):
    return f"""  <section class="section">
    <div class="wrap">
      <div class="page-cta">
        <div>
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <div class="page-cta__actions">
          <a class="btn btn--ember btn--lg" href="tel:{TEL_HREF}">{ARROW} {TEL_TXT}</a>
          <a class="btn btn--onDark btn--lg" href="index.html#contacto">Pedir cita</a>
        </div>
      </div>
    </div>
  </section>
"""
