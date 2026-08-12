/* ============================================================================
   [NOMBRE CLÍNICA] · Interacción y movimiento
   Todo el movimiento usa transform/opacity (sin layout thrashing) y se apaga
   entero con prefers-reduced-motion.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGSAP = typeof window.gsap !== 'undefined';

  /* Si GSAP no está disponible (CDN caída, sin red), se devuelve la visibilidad
     al contenido inmediatamente: la página nunca queda en blanco. */
  if (!hasGSAP || reduceMotion) root.classList.remove('js');

  /* --------------------------------------------------------------- Año */
  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  /* ------------------------------------------- Vídeo de bienvenida del hero */
  /* Carga condicional: el póster se queda si el usuario pide menos movimiento
     o tiene activo el ahorro de datos. En móvil se sirve la versión ligera.
     Como el vídeo ya no está en la primera pantalla, se descarga solo cuando
     se acerca: así no compite con el primer pintado. */
  (function initHeroVideo() {
    var v = document.querySelector('.hero__video');
    if (!v) return;
    var conn = navigator.connection || {};
    if (reduceMotion || conn.saveData) return;

    function load() {
      var small = window.matchMedia('(max-width: 700px)').matches;
      var src = small ? v.getAttribute('data-src-sm') : v.getAttribute('data-src-lg');
      if (!src || v.getAttribute('src')) return;
      v.setAttribute('src', src);
      v.load();
      var played = v.play();
      if (played && typeof played.catch === 'function') {
        played.catch(function () { /* autoplay bloqueado: se mantiene el póster */ });
      }
    }

    var host = document.querySelector('.hero__scroll') || v;
    if (!('IntersectionObserver' in window)) { load(); return; }
    var io = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) { load(); io.disconnect(); }
    }, { rootMargin: '600px 0px' });
    io.observe(host);
  })();

  /* --------------------------------------------------- Menú de navegación */
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

  /* ---------------- Píldora flotante, dock móvil y barra de progreso -------- */
  /* La barra no es una franja fija: es una píldora que flota arriba y se
     esconde al bajar (para no molestar en los momentos inmersivos), volviendo
     en cuanto se sube. */
  var dock = document.querySelector('.dock');
  var spineFill = document.querySelector('.vitals-spine__fill');
  var lastY = window.scrollY;
  var navHidden = false;
  var ticking = false;

  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      var y = window.scrollY;

      if (nav) {
        nav.classList.toggle('is-stuck', y > 10);

        /* Con "reducir movimiento" o con el menú abierto se mantiene visible. */
        var menuOpen = menu && menu.classList.contains('is-open');
        if (!reduceMotion && !menuOpen) {
          if (y < 40) navHidden = false;
          else if (y > lastY + 3 && y > 140) navHidden = true;
          else if (y < lastY - 3) navHidden = false;
        } else {
          navHidden = false;
        }
        nav.classList.toggle('is-hidden', navHidden);
      }

      if (dock) dock.classList.toggle('is-visible', y > 620);
      if (spineFill) {
        var max = document.body.scrollHeight - window.innerHeight;
        var p = max > 0 ? Math.min(y / max, 1) : 0;
        spineFill.style.transform = 'scaleY(' + p.toFixed(4) + ')';
      }
      lastY = y;
      ticking = false;
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();

  /* ------------------------------- Desplazamiento suave de enlaces internos */
  /* Sustituye a `scroll-behavior: smooth` en CSS, que rompía las medidas de
     ScrollTrigger al redimensionar o hacer zoom (ver nota en styles.css).
     Aquí solo se suaviza el clic del usuario, nunca los saltos internos que
     GSAP necesita instantáneos. */
  (function initSmoothAnchors() {
    var NAV_OFFSET = 96;   /* mismo valor que scroll-padding-top */

    document.addEventListener('click', function (e) {
      var link = e.target.closest ? e.target.closest('a[href^="#"]') : null;
      if (!link) return;
      var id = link.getAttribute('href');
      if (!id || id === '#' || id.length < 2) return;

      var target = document.getElementById(id.slice(1));
      if (!target) return;

      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.scrollY - NAV_OFFSET;
      window.scrollTo({
        top: Math.max(0, top),
        behavior: reduceMotion ? 'auto' : 'smooth'
      });

      /* La URL y el foco deben seguir al scroll: si no, el enlace no sirve
         para quien navega con teclado o comparte el enlace. */
      if (history.replaceState) history.replaceState(null, '', id);
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    });
  })();

  /* --------------------------------------------- Sección activa en el menú */
  /* Solo se espían los enlaces de ancla: si el menú incluyera una página
     (.html), querySelector lanzaría un error de selector no válido. */
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav__links a'))
    .filter(function (a) { return (a.getAttribute('href') || '').charAt(0) === '#'; });
  var sections = links
    .map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); })
    .filter(Boolean);

  if ('IntersectionObserver' in window && sections.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          a.classList.toggle('is-current', a.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ====================================================================
     TRIAJE — orientación según especie y motivo.
     Redactado con criterio clínico divulgativo: nunca sustituye consulta.
     ==================================================================== */
  var TEL = 'tel:+34910305305';   /* Clínica Veterinaria Vitalis — identidad de muestra */

  var MOTIVOS = {
    apetito: {
      level: 'now',
      badge: 'Hoy, sin esperar',
      title: 'Dejar de comer nunca es «ya se le pasará»',
      text: 'Un animal que no come ni bebe se deshidrata rápido y suele estar avisando de dolor, fiebre o una obstrucción. Queremos verle hoy.',
      service: 'Consulta de urgencia + analítica'
    },
    digestivo: {
      level: 'now',
      badge: 'Hoy, sin esperar',
      title: 'Vómitos o diarrea: lo que importa es cuántos y cómo',
      text: 'Si son repetidos, hay sangre, decaimiento o lleva más de 12 horas así, vente hoy. La deshidratación avanza más deprisa de lo que parece.',
      service: 'Consulta de urgencia + fluidoterapia'
    },
    trauma: {
      level: 'now',
      badge: 'Urgencia',
      title: 'Un golpe se valora entero, no solo la pata',
      text: 'Tras una caída o un atropello puede haber daño interno sin herida visible. No le des analgésicos humanos: muchos son tóxicos. Tráelo con el mínimo movimiento posible.',
      service: 'Urgencias · traumatología'
    },
    herida: {
      level: 'now',
      badge: 'Urgencia',
      title: 'Sangrado o bulto: mejor hoy que el lunes',
      text: 'Presiona la herida con una gasa limpia durante el trayecto. Si es un bulto que ha crecido o cambiado en semanas, hay que verlo y, probablemente, puncionarlo.',
      service: 'Urgencias · cirugía'
    },
    respira: {
      level: 'now',
      badge: 'Emergencia',
      title: 'La dificultad respiratoria no espera',
      text: 'Sal hacia la clínica y llámanos por el camino. Mantén el ambiente fresco, no lo abraces contra el pecho y evita el transportín cerrado si se agobia.',
      service: 'Urgencias · oxigenoterapia'
    },
    preventiva: {
      level: 'plan',
      badge: 'Con cita tranquila',
      title: 'Perfecto: esto se planifica',
      text: 'Revisión completa, calendario de vacunas según su edad y forma de vida, desparasitación y chip con alta en el registro. En una sola visita.',
      service: 'Consulta preventiva'
    },
    cirugia: {
      level: 'soon',
      badge: 'Valoración esta semana',
      title: 'Toda cirugía empieza con una valoración',
      text: 'Exploramos, hacemos la analítica preanestésica y te damos el presupuesto cerrado y las pautas de ayuno por escrito. Si ya está operado y algo no va bien, llámanos hoy.',
      service: 'Consulta prequirúrgica'
    }
  };

  /* Matices por especie: donde la especie cambia de verdad el consejo. */
  var NOTAS = {
    'gato|apetito': 'En gatos es especialmente serio: más de 24 h sin comer puede desencadenar una lipidosis hepática. No esperes al fin de semana.',
    'gato|respira': 'Un gato que respira con la boca abierta o con el cuello estirado es una emergencia inmediata. Llámanos y sal ya.',
    'gato|digestivo': 'Si vomita y no consigue orinar, sospechamos obstrucción urinaria: en machos es una emergencia vital.',
    'perro|digestivo': 'Si intenta vomitar sin sacar nada y tiene el abdomen hinchado y duro, puede ser una torsión gástrica. Eso es quirófano inmediato.',
    'perro|apetito': 'En razas grandes, dejar de comer con decaimiento súbito obliga a descartar torsión y problemas de bazo el mismo día.',
    'perro|trauma': 'Aunque camine, un atropello exige radiografía y control de tensión: las hemorragias internas tardan horas en dar la cara.',
    'otro|apetito': 'En conejos y roedores, dejar de comer más de 12 h es una urgencia digestiva grave. Llámanos antes de venir.',
    'otro|digestivo': 'En conejos y roedores, dejar de comer más de 12 h es una urgencia digestiva grave. Llámanos antes de venir.',
    'otro|respira': 'En aves y pequeños mamíferos la dificultad respiratoria avanza muy rápido. Llama antes de salir.',
    'otro|preventiva': 'Con animales exóticos, llámanos primero: te confirmamos si podemos atenderle o a qué centro de referencia derivarte.',
    'otro|cirugia': 'Con animales exóticos, llámanos primero: te confirmamos si podemos atenderle o a qué centro de referencia derivarte.'
  };

  var estado = { especie: 'perro', motivo: 'apetito' };
  var resultBox = document.getElementById('triage-result');

  function escapeHTML(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function renderTriage(animate) {
    if (!resultBox) return;
    var data = MOTIVOS[estado.motivo];
    if (!data) return;

    var nota = NOTAS[estado.especie + '|' + estado.motivo];
    var urgente = data.level === 'now';

    var html =
      '<div class="result">' +
        '<div>' +
          '<div class="result__head">' +
            '<span class="result__badge result__badge--' + data.level + '">' + escapeHTML(data.badge) + '</span>' +
            '<span class="result__service">' + escapeHTML(data.service) + '</span>' +
          '</div>' +
          '<h3 class="result__title">' + escapeHTML(data.title) + '</h3>' +
          '<p class="result__text">' + escapeHTML(data.text) + '</p>' +
          (nota ? '<p class="result__note">' + escapeHTML(nota) + '</p>' : '') +
        '</div>' +
        '<div class="result__actions">' +
          (urgente
            ? '<a class="btn btn--ember" href="' + TEL + '">Llamar a urgencias</a>'
            : '<a class="btn btn--solid" href="#contacto">Pedir cita</a>' +
              '<a class="btn btn--outline" href="' + TEL + '">Llamar</a>') +
        '</div>' +
      '</div>';

    resultBox.innerHTML = html;

    if (animate && hasGSAP && !reduceMotion) {
      window.gsap.from(resultBox.firstChild, {
        opacity: 0, y: 10, duration: 0.32, ease: 'power2.out'
      });
    }
  }

  Array.prototype.forEach.call(document.querySelectorAll('.chips'), function (group) {
    var key = group.getAttribute('data-group') === 'especie' ? 'especie' : 'motivo';
    group.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip');
      if (!chip || !group.contains(chip)) return;
      Array.prototype.forEach.call(group.querySelectorAll('.chip'), function (c) {
        var active = c === chip;
        c.classList.toggle('is-active', active);
        c.setAttribute('aria-pressed', String(active));
      });
      estado[key] = chip.getAttribute('data-value');
      renderTriage(true);
    });
  });

  renderTriage(false);

  /* ====================================================================
     FORMULARIO — honeypot, validación en cliente y mensajes junto al campo
     ==================================================================== */
  var form = document.getElementById('form-contacto');

  if (form) {
    var ts = document.getElementById('form_ts');
    if (ts) ts.value = String(Date.now());

    var status = document.getElementById('form-status');

    function setError(input, on) {
      var field = input.closest('.field') || input.closest('.consent');
      var err = document.getElementById('err-' + input.id);
      if (field) field.classList.toggle('has-error', on);
      if (err) err.hidden = !on;
      input.setAttribute('aria-invalid', String(on));
    }

    function validate(input) {
      var v = (input.value || '').trim();
      var ok = true;

      if (input.type === 'checkbox') ok = input.checked;
      else if (input.required && !v) ok = false;
      else if (input.type === 'tel' && v) ok = v.replace(/\D/g, '').length >= 9;
      else if (input.type === 'email' && v) ok = /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v);
      else if (input.id === 'mensaje' && v) ok = v.length >= 10;

      setError(input, !ok);
      return ok;
    }

    var required = ['nombre', 'telefono', 'mensaje', 'privacidad'];
    var optional = ['email'];

    /* Se valida al salir del campo y, si ya estaba en error, mientras se corrige:
       nunca se interrumpe a alguien que aún está escribiendo. */
    required.concat(optional).forEach(function (id) {
      var el = document.getElementById(id);
      if (!el) return;

      if (el.type === 'checkbox') {
        el.addEventListener('change', function () { validate(el); });
        return;
      }

      el.addEventListener('blur', function () { validate(el); });
      el.addEventListener('input', function () {
        var box = el.closest('.field');
        if (box && box.classList.contains('has-error')) validate(el);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      /* Honeypot: si un bot rellena el campo señuelo, se descarta en silencio.
         TODO SERVIDOR: repetir esta comprobación en el backend; el cliente
         nunca es una barrera de seguridad por sí solo. */
      var hp = document.getElementById('hp-website');
      if (hp && hp.value !== '') return;

      /* Envío demasiado rápido (< 3 s) = comportamiento automatizado. */
      var started = parseInt((document.getElementById('form_ts') || {}).value || '0', 10);
      if (started && Date.now() - started < 3000) return;

      var firstBad = null;
      required.forEach(function (id) {
        var el = document.getElementById(id);
        if (el && !validate(el) && !firstBad) firstBad = el;
      });
      var mail = document.getElementById('email');
      if (mail && mail.value.trim() && !validate(mail) && !firstBad) firstBad = mail;

      if (firstBad) {
        if (status) {
          status.textContent = 'Revisa los campos marcados para poder enviar la solicitud.';
          status.className = 'form__status is-error';
        }
        firstBad.focus();
        return;
      }

      /* TODO SERVIDOR: sustituir por el POST real (fetch a /api/contacto),
         con validación, rate limiting y cifrado en tránsito. */
      if (status) {
        status.textContent = 'Solicitud preparada. Conecta el formulario al servidor para enviarla de verdad.';
        status.className = 'form__status is-ok';
      }
    });
  }

  /* ====================================================================
     MOVIMIENTO (GSAP)
     ==================================================================== */
  if (!hasGSAP || reduceMotion) return;

  var gsap = window.gsap;
  if (window.ScrollTrigger) {
    gsap.registerPlugin(window.ScrollTrigger);
    /* En móvil, mostrar/ocultar la barra del navegador cambia la altura del
       viewport y dispara refrescos constantes que dan tirones. Con esto solo
       se refresca cuando cambia la ANCHURA (giro de pantalla), que es cuando
       de verdad cambia la maquetación. */
    window.ScrollTrigger.config({ ignoreMobileResize: true });
  }

  gsap.defaults({ ease: 'power2.out' });

  /* Entrada del hero: una sola secuencia, no efectos sueltos. */
  var heroItems = gsap.utils.toArray('.js-hero');

  gsap.timeline({ delay: 0.1 })
    .set(heroItems, { opacity: 0 })
    .to(heroItems, {
      opacity: 1,
      y: 0,
      duration: 0.62,
      stagger: 0.085,
      startAt: { y: 26 }
    });

  /* Sin ScrollTrigger no hay revelado por scroll: se devuelve la visibilidad
     para que nada quede oculto de forma permanente. */
  if (!window.ScrollTrigger) {
    gsap.set('.js-reveal', { opacity: 1, clearProps: 'opacity' });
  }

  if (window.ScrollTrigger) {
    var ST = window.ScrollTrigger;

    /* ------------------------------------------------------------ REVELADOS
       En lote (batch), no uno a uno: los elementos que entran juntos en
       pantalla se escalonan entre sí, que es como el ojo espera leerlos. */
    ST.batch('.js-reveal', {
      start: 'top 88%',
      once: true,
      onEnter: function (batch) {
        gsap.fromTo(batch,
          { opacity: 0, y: 30 },
          {
            opacity: 1, y: 0, duration: 0.7, ease: 'expo.out',
            stagger: { each: 0.08, from: 'start' }
          }
        );
      }
    });

    /* Encabezados de sección: epígrafe, título y entradilla en cascada corta. */
    gsap.utils.toArray('.section__head').forEach(function (head) {
      var parts = head.querySelectorAll('.eyebrow, .section__title, .section__lede');
      if (!parts.length) return;
      gsap.fromTo(parts,
        { opacity: 0, y: 22 },
        {
          opacity: 1, y: 0, duration: 0.7, ease: 'expo.out', stagger: 0.09,
          scrollTrigger: { trigger: head, start: 'top 86%', once: true }
        }
      );
    });

    /* Parallax de las fotos de instalaciones dentro de su marco: da
       profundidad sin mover el texto. Se anima el <picture>, no la <img>: así
       el zoom al pasar el ratón (que es CSS sobre la img) sigue funcionando y
       no pelean por transform. El marco recorta, por eso la foto va un pelín
       sobredimensionada.
       El equipo ya no lleva esta clase: sus tarjetas tienen su propio
       movimiento (el giro 3D en assets/js/team-flip.js) y mezclarlo con este
       parallax pelearía por el mismo transform. */
    gsap.utils.toArray('.shot picture').forEach(function (pic) {
      var host = pic.closest('.shot');
      if (!host) return;
      gsap.set(pic, { scale: 1.09, transformOrigin: 'center center' });
      gsap.fromTo(pic,
        { yPercent: -3 },
        {
          yPercent: 3, ease: 'none',
          scrollTrigger: { trigger: host, start: 'top bottom', end: 'bottom top', scrub: true }
        }
      );
    });

    /* Numeración de "Tu visita": aparece marcando el paso. */
    gsap.utils.toArray('.step__num').forEach(function (num) {
      gsap.fromTo(num,
        { opacity: 0, x: -14 },
        {
          opacity: 1, x: 0, duration: 0.5, ease: 'back.out(2)',
          scrollTrigger: { trigger: num.closest('.step'), start: 'top 84%', once: true }
        }
      );
    });

    /* Banda de urgencias: entra con cuerpo, es la llamada más importante. */
    var urgent = document.querySelector('.urgent__inner');
    if (urgent) {
      gsap.fromTo(urgent.children,
        { opacity: 0, y: 26 },
        {
          opacity: 1, y: 0, duration: 0.8, ease: 'expo.out', stagger: 0.12,
          scrollTrigger: { trigger: urgent, start: 'top 85%', once: true }
        }
      );
    }

    /* Rollo de película: el mensaje gira y se desvanece al empezar a bajar. */
    var introItems = gsap.utils.toArray('.hero__intro > *');
    if (introItems.length) {
      var introTl = gsap.timeline({
        scrollTrigger: { trigger: '.hero__stage', start: 'top top', end: 'top+=480 top', scrub: 1.1 }
      });
      introItems.forEach(function (el, i) {
        introTl.to(el, {
          rotationX: 90,
          y: -30,
          scale: 0.7,
          opacity: 0,
          filter: 'blur(4px)',
          ease: 'power3.inOut',
          transformOrigin: 'center top'
        }, i * 0.08);
      });
      gsap.to('.scroll-hint', {
        opacity: 0, ease: 'none',
        scrollTrigger: { trigger: '.hero__stage', start: 'top top', end: 'top+=200 top', scrub: true }
      });
    }

    /* El vídeo crece hasta llenar la pantalla y descubre el mensaje. */
    if (document.querySelector('.hero__scroll')) {
      gsap.timeline({
        scrollTrigger: { trigger: '.hero__scroll', start: 'top top', end: 'bottom bottom', scrub: 1.1 }
      })
        .to('.hero__video-frame', {
          width: '94vw', height: '90svh', borderRadius: 0,
          ease: 'expo.out', duration: 0.5
        }, 0)
        .to('.hero__video', { scale: 1.08, ease: 'expo.out', duration: 0.5 }, 0)
        .to('.hero__video-overlay', {
          clipPath: 'inset(0% 0 0 0)', ease: 'expo.out', duration: 0.3
        }, 0.4)
        .fromTo('.hero__video-caption', { y: 30 },
          { y: 0, ease: 'expo.out', duration: 0.3 }, 0.45)
        .fromTo('.hero__video-content', { filter: 'blur(10px)', scale: 1.1 },
          { filter: 'blur(0px)', scale: 1, ease: 'expo.out', duration: 0.4 }, 0.45);

      gsap.from('.trust-card', {
        opacity: 0, y: 14, scale: 0.92, duration: 0.6, ease: 'back.out(1.6)',
        scrollTrigger: { trigger: '.hero__scroll', start: 'top 78%', once: true }
      });
    }

    /* ---------------------------------------------------------- OPINIONES
       Tres actos, no uno: las fotos se acercan, el titular se afianza y luego
       TODO sale de cuadro pasando de largo. Sin ese tercer acto el zoom se
       cortaba en seco y el carrusel entraba a destiempo. */
    if (document.querySelector('.zoomwall')) {
      var wallTl = gsap.timeline({
        scrollTrigger: {
          trigger: '.zoomwall', start: 'top top', end: '+=230%', pin: true, scrub: 1,
          invalidateOnRefresh: true,   /* al redimensionar, vuelve a tomar medidas */
          anticipatePin: 1
        }
      });

      /* Acto 1 (0 → 0.55): el collage se acerca y el titular emerge. */
      wallTl
        .to(".zoomwall__item[data-layer='3']", { opacity: 1, z: 560, ease: 'power1.inOut', duration: 0.55 }, 0)
        .to(".zoomwall__item[data-layer='2']", { opacity: 1, z: 440, ease: 'power1.inOut', duration: 0.55 }, 0)
        .to(".zoomwall__item[data-layer='1']", { opacity: 1, z: 320, ease: 'power1.inOut', duration: 0.55 }, 0)
        .to('.zoomwall__title', { opacity: 1, z: 50, ease: 'power1.inOut', duration: 0.55 }, 0)

      /* Acto 2 (0.55 → 0.70): respiro. El titular se queda solo, legible. */
        .to({}, { duration: 0.15 })

      /* Acto 3 (0.70 → 1): las fotos pasan de largo junto a la cámara y se
         desvanecen; el titular las sigue al final. Deja el lienzo limpio
         justo antes del carrusel.
         Se agranda con `scale`, no con más `z`: pasado el plano de la cámara
         (perspective: 100svh) la proyección se invierte y las fotos, en vez de
         seguir creciendo, encogen de golpe. `scale` no tiene esa singularidad
         y se comporta igual sea cual sea el alto de la ventana. */
        .to(".zoomwall__item[data-layer='3']", { scale: 2.6, opacity: 0, ease: 'power2.in', duration: 0.3 }, 0.70)
        .to(".zoomwall__item[data-layer='2']", { scale: 2.3, opacity: 0, ease: 'power2.in', duration: 0.3 }, 0.73)
        .to(".zoomwall__item[data-layer='1']", { scale: 2.0, opacity: 0, ease: 'power2.in', duration: 0.3 }, 0.76)
        .to('.zoomwall__title', {
          scale: 1.28, opacity: 0, filter: 'blur(6px)', ease: 'power2.in', duration: 0.26
        }, 0.80);

      /* El carrusel entra al terminar el collage, no antes: sube y se aclara. */
      var mqBlock = document.querySelector('#opiniones .reviews-marquee-block');
      if (mqBlock) {
        gsap.from(mqBlock, {
          opacity: 0, y: 60, filter: 'blur(6px)', duration: 0.9, ease: 'expo.out',
          scrollTrigger: { trigger: mqBlock, start: 'top 92%', once: true }
        });
        gsap.from('#opiniones .mini-review', {
          opacity: 0, y: 26, duration: 0.55, stagger: 0.06, ease: 'power2.out',
          scrollTrigger: { trigger: mqBlock, start: 'top 88%', once: true }
        });
      }
    }

    /* Contadores de las cifras. */
    gsap.utils.toArray('.stat__num[data-count]').forEach(function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      var obj = { v: 0 };
      gsap.to(obj, {
        v: target,
        duration: 1.4,
        ease: 'power1.out',
        scrollTrigger: { trigger: el, start: 'top 92%', once: true },
        onUpdate: function () { el.textContent = Math.round(obj.v) + suffix; }
      });
    });

    window.addEventListener('load', function () { window.ScrollTrigger.refresh(); });
  }
})();
