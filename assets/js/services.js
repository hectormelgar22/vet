/* ============================================================================
   Servicios · lista con banda deslizante e imagen sincronizada
   Adaptado de un componente GSAP (lista + media). Cambios de fondo respecto al
   original, explicados en assets/css/services.css y en el README:
     · la banda no usa mix-blend-mode, sino una copia clara recortada
     · los textos viven en el HTML (indexables), no en un array de JS
     · sin JS la sección sigue leyéndose entera
   ========================================================================== */
(function () {
  'use strict';

  var section = document.querySelector('.svc');
  if (!section) return;

  var rowsWrap = section.querySelector('.svc__rows');
  var rows = Array.prototype.slice.call(section.querySelectorAll('.svc__row'));
  var media = section.querySelector('.svc__media');
  var caption = section.querySelector('.svc__caption');
  var panels = Array.prototype.slice.call(section.querySelectorAll('.svc__panel'));
  var cta = section.querySelector('.svc__cta');
  var strip = section.querySelector('.svc__strip');
  if (!rows.length || !strip) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia('(pointer: fine)').matches;
  var hasGSAP = typeof window.gsap !== 'undefined';
  var gsap = window.gsap;
  var active = 0;

  /* ---- La copia clara que vive dentro de la banda ------------------------ */
  /* Se clona en vez de duplicarla en el HTML: una sola fuente de verdad para
     los nombres de los servicios. */
  var clone = rowsWrap.cloneNode(true);
  clone.removeAttribute('id');
  clone.setAttribute('aria-hidden', 'true');
  if ('inert' in HTMLElement.prototype) clone.inert = true;
  clone.removeAttribute('role');
  clone.removeAttribute('aria-label');
  /* La copia es puramente visual: se le quitan enlace, id y roles para que no
     duplique destinos ante los buscadores ni sea alcanzable con el tabulador. */
  clone.querySelectorAll('a').forEach(function (a) {
    a.removeAttribute('href');
    a.removeAttribute('id');
    a.removeAttribute('role');
    a.removeAttribute('aria-current');
    a.tabIndex = -1;
  });
  strip.appendChild(clone);
  var cloneRows = Array.prototype.slice.call(clone.querySelectorAll('.svc__row'));

  /* Filas reales y su copia deben moverse EXACTAMENTE igual en la entrada: si
     solo se animan las reales, la copia de dentro de la banda queda desfasada
     y se ve el texto duplicado y descuadrado. El stagger empareja por índice. */
  var allRows = rows.concat(cloneRows);
  var pairStagger = function (i) { return (i % rows.length) * 0.07; };

  /* ---- Estado base sin JS revertido ------------------------------------- */
  panels.forEach(function (p, i) {
    p.style.visibility = i === active ? 'visible' : 'hidden';
    if (i !== active) p.style.opacity = '0';
  });

  /* ---- La banda ---------------------------------------------------------- */
  function placeStrip(index, instant) {
    var row = rows[index];
    if (!row) return;
    var top = row.offsetTop;
    var h = row.offsetHeight;
    if (!hasGSAP || instant || reduceMotion) {
      strip.style.height = h + 'px';
      strip.style.transform = 'translateY(' + top + 'px)';
      clone.style.transform = 'translateY(' + (-top) + 'px)';
      return;
    }
    var opts = { duration: 0.46, ease: 'power3.out', overwrite: true };
    gsap.to(strip, Object.assign({ y: top, height: h }, opts));
    gsap.to(clone, Object.assign({ y: -top }, opts));
  }

  /* ---- La imagen: cada cambio apila una capa nueva ----------------------- */
  function swapImage(row) {
    var base = row.getAttribute('data-img');
    if (!base) return;

    var layer = document.createElement('div');
    layer.className = 'svc__layer';

    var pic = document.createElement('picture');
    var src = document.createElement('source');
    src.type = 'image/webp';
    src.srcset = base + '.webp';
    var img = document.createElement('img');
    img.src = base + '.jpg';
    img.alt = row.getAttribute('data-alt') || '';
    img.width = 900; img.height = 1120;
    img.decoding = 'async';
    pic.appendChild(src);
    pic.appendChild(img);
    layer.appendChild(pic);
    media.insertBefore(layer, media.querySelector('.svc__caption'));

    if (!hasGSAP || reduceMotion) {
      while (layer.previousElementSibling &&
             layer.previousElementSibling.classList.contains('svc__layer')) {
        layer.previousElementSibling.remove();
      }
      return;
    }

    gsap.set(layer, { clipPath: 'inset(50%)' });
    gsap.set(pic, { scale: 1.35 });
    gsap.timeline({
      onComplete: function () {
        /* esta capa ya tapa entera a las de debajo: se limpian */
        while (layer.previousElementSibling &&
               layer.previousElementSibling.classList.contains('svc__layer')) {
          layer.previousElementSibling.remove();
        }
      }
    })
      .to(layer, { clipPath: 'inset(0%)', duration: 0.72, ease: 'power3.inOut' }, 0)
      .to(pic, { scale: 1, duration: 1.05, ease: 'power2.out' }, 0);
  }

  /* ---- La descripción: entra por líneas ---------------------------------- */
  function revealPanel(panel, instant) {
    var desc = panel.querySelector('.svc__desc');
    var tags = panel.querySelector('.svc__tags');
    panel.style.visibility = 'visible';

    if (!hasGSAP || reduceMotion || instant) {
      panel.style.opacity = '1';
      return;
    }

    gsap.set(panel, { opacity: 1 });

    /* SplitText (gratuito desde GSAP 3.13) da el revelado línea a línea con
       máscara. Si no está disponible, el bloque entero entra deslizándose:
       menos fino, pero nunca se queda sin animación ni sin texto. */
    if (window.SplitText && desc) {
      var split = new window.SplitText(desc, { type: 'lines', mask: 'lines' });
      panel._split = split;
      gsap.fromTo(split.lines, { yPercent: 110 }, {
        yPercent: 0, duration: 0.62, stagger: 0.055, ease: 'power3.out',
        onComplete: function () {
          split.revert();       /* se deshace para que el texto reflote al redimensionar */
          delete panel._split;
        }
      });
    } else if (desc) {
      gsap.fromTo(desc, { y: 22, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.55, ease: 'power3.out' });
    }

    if (tags) {
      gsap.fromTo(tags.children, { y: 14, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.45, stagger: 0.045, ease: 'power2.out', delay: 0.12 });
    }
  }

  function hidePanel(panel) {
    if (!hasGSAP || reduceMotion) {
      panel.style.visibility = 'hidden';
      panel.style.opacity = '0';
      return;
    }
    if (panel._split) { panel._split.revert(); delete panel._split; }
    gsap.killTweensOf(panel.querySelectorAll('.svc__desc, .svc__tags > *'));
    gsap.to(panel, {
      opacity: 0, y: -14, duration: 0.22, ease: 'power2.in',
      onComplete: function () {
        panel.style.visibility = 'hidden';
        gsap.set(panel, { y: 0 });
      }
    });
  }

  /* ---- La flecha sale por arriba y vuelve a entrar por abajo ------------- */
  function swapArrow() {
    if (!hasGSAP || reduceMotion || !cta) return;
    var arrow = cta.querySelector('svg');
    if (!arrow) return;
    gsap.killTweensOf(arrow);
    gsap.timeline({ defaults: { ease: 'none' } })
      .to(arrow, { x: 40, y: -40, duration: 0.13 })
      .set(arrow, { x: -40, y: 40 })
      .to(arrow, { x: 0, y: 0, duration: 0.17 });
  }

  /* ---- Activación -------------------------------------------------------- */
  function setActive(index, instant) {
    if (index === active && !instant) return;
    var prev = active;
    active = index;

    rows.forEach(function (r, i) {
      r.classList.toggle('is-active', i === index);
      if (i === index) r.setAttribute('aria-current', 'true');
      else r.removeAttribute('aria-current');
    });

    var row = rows[index];
    if (caption) caption.textContent = row.getAttribute('data-caption') || row.textContent.trim();
    /* La flecha lleva al servicio que se está viendo, no a uno fijo. */
    if (cta) {
      cta.setAttribute('href', row.getAttribute('href'));
      cta.setAttribute('aria-label', 'Ver la página de ' + (row.getAttribute('data-name') || 'este servicio'));
    }

    if (!instant) {
      if (panels[prev] && prev !== index) hidePanel(panels[prev]);
      swapImage(row);
      swapArrow();
    }
    if (panels[index]) revealPanel(panels[index], instant);
    placeStrip(index, instant);
  }

  /* ---- Cada fila es un enlace a su página ------------------------------- */
  /* Al enfocarla con el tabulador o pasar el ratón se previsualiza; al pulsar,
     el navegador sigue el enlace (no se intercepta el clic). */
  rows.forEach(function (row, i) {
    row.addEventListener('focus', function () { setActive(i); });
    row.addEventListener('mouseenter', function () { setActive(i); });
  });

  /* ---- Hover que también funciona mientras se hace scroll ---------------- */
  /* El navegador no dispara eventos de hover cuando la página se mueve bajo un
     cursor quieto. Se guarda la posición del puntero y se comprueba qué hay
     debajo también en cada scroll, con rAF para no medir de más. */
  if (finePointer && !reduceMotion) {
    var px = -1, py = -1, queued = false, hovered = null;

    function hitTest() {
      queued = false;
      if (px < 0) return;
      var el = document.elementFromPoint(px, py);
      var row = el && el.closest ? el.closest('.svc__row') : null;
      if (row && (!section.contains(row) || strip.contains(row))) row = null;
      if (row !== hovered) {
        if (hovered) hovered.classList.remove('is-hovered');
        hovered = row;
        if (hovered) hovered.classList.add('is-hovered');
      }
      if (row) {
        var i = rows.indexOf(row);
        if (i > -1) setActive(i);
      }
    }
    function queue() { if (!queued) { queued = true; requestAnimationFrame(hitTest); } }

    window.addEventListener('pointermove', function (e) {
      px = e.clientX; py = e.clientY; queue();
    }, { passive: true });
    window.addEventListener('scroll', queue, { passive: true });

  } else if ('IntersectionObserver' in window) {
    /* Sin ratón no hay previsualización posible al pasar por encima, y la foto
       se quedaría siempre en el primer servicio. Aquí manda el scroll: la fila
       que cruza el centro de la pantalla es la que se muestra arriba. */
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = rows.indexOf(en.target);
        if (i > -1) setActive(i);
      });
    }, { rootMargin: '-48% 0px -48% 0px' });
    rows.forEach(function (r) { io.observe(r); });
  }

  /* ---- Recolocar la banda cuando cambian fuentes o tamaño ---------------- */
  function reposition() { placeStrip(active, true); }
  window.addEventListener('resize', reposition, { passive: true });
  window.addEventListener('load', reposition);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(reposition);

  /* ---- Entrada al llegar a la sección ------------------------------------ */
  setActive(0, true);

  if (!hasGSAP || reduceMotion || !window.ScrollTrigger) {
    strip.style.opacity = '1';
    return;
  }

  var firstLayer = media.querySelector('.svc__layer');
  gsap.set(strip, { autoAlpha: 0 });
  gsap.set(allRows, { autoAlpha: 0, y: 40 });
  if (firstLayer) {
    gsap.set(firstLayer, { clipPath: 'inset(50%)' });
    gsap.set(firstLayer.querySelector('picture, img'), { scale: 1.3 });
  }
  if (caption) gsap.set(caption, { autoAlpha: 0, y: 14 });
  if (panels[0]) gsap.set(panels[0], { autoAlpha: 0 });
  if (cta) gsap.set(cta, { autoAlpha: 0, scale: 0.65 });

  window.ScrollTrigger.create({
    trigger: section,
    start: 'top 72%',
    once: true,
    onEnter: function () {
      /* Las demás imágenes se piden ahora, no al cargar la página: así no
         compiten con lo que se ve primero. */
      rows.forEach(function (r) {
        var b = r.getAttribute('data-img');
        if (b) { var im = new Image(); im.src = b + '.webp'; }
      });

      var tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
      if (firstLayer) {
        tl.to(firstLayer, { clipPath: 'inset(0%)', duration: 0.95, ease: 'power3.inOut' }, 0)
          .to(firstLayer.querySelector('picture, img'), { scale: 1, duration: 1.6, ease: 'power2.out' }, 0);
      }
      if (caption) tl.to(caption, { autoAlpha: 1, y: 0, duration: 0.5 }, 0.5);
      tl.to(allRows, { autoAlpha: 1, y: 0, duration: 0.8, stagger: pairStagger }, 0.22)
        .add(function () { placeStrip(active, true); }, 0.24)
        .to(strip, { autoAlpha: 1, duration: 0.45 }, 0.72)
        .add(function () { if (panels[0]) { gsap.set(panels[0], { autoAlpha: 1 }); revealPanel(panels[0]); } }, 0.6);
      if (cta) tl.to(cta, { autoAlpha: 1, scale: 1, duration: 0.55, ease: 'back.out(1.7)' }, 0.8);
      tl.add(function () { placeStrip(active, true); });
    }
  });
})();
