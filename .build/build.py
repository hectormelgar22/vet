# -*- coding: utf-8 -*-
"""Ensambla las páginas interiores.  Uso:  python .build/build.py"""
import os, sys, json, io

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)

from pagegen import (head, NAV, footer, COOKIE_BANNER, breadcrumb, page_cta,
                     BRAND, SITE, TEL_HREF, TEL_TXT, MAIL)
from legal import LEGALES, DRAFT
from servicios import SERVICIOS
from guias import GUIAS

SVC_BY_SLUG = {s["slug"]: s for s in SERVICIOS}


def qa(items):
    out = []
    for i, (q, a) in enumerate(items):
        op = " open" if i == 0 else ""
        out.append(f"""        <details class="qa"{op}>
          <summary>
            <span>{q}</span>
            <span class="qa__sign" aria-hidden="true"></span>
          </summary>
          <div class="qa__body"><p>{a}</p></div>
        </details>""")
    return "\n".join(out)


def faq_jsonld(items):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>")


def breadcrumb_jsonld(title, slug):
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": title, "item": f"{SITE}/{slug}.html"},
        ],
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>")


def service_jsonld(s):
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": s["name"],
        "serviceType": s["nav"],
        "description": s["meta"],
        "url": f"{SITE}/{s['slug']}.html",
        "areaServed": {"@type": "City", "name": "Madrid"},
        "provider": {
            "@type": "VeterinaryCare",
            "name": BRAND,
            "telephone": TEL_HREF,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Calle de Alcalá, 415",
                "postalCode": "28027",
                "addressLocality": "Madrid",
                "addressCountry": "ES",
            },
        },
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>")


def article_jsonld(g):
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": g["h1"],
        "description": g["meta"],
        "inLanguage": "es",
        "datePublished": g["updated"],
        "dateModified": g["updated"],
        "image": f"{SITE}/assets/img/og-cover.jpg",
        "author": {"@type": "Organization", "name": BRAND, "url": f"{SITE}/"},
        "publisher": {
            "@type": "Organization",
            "name": BRAND,
            "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/img/og-cover.jpg"},
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}/{g['slug']}.html"},
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>")


def write(path, content):
    with io.open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return path


# --------------------------------------------------------------- LEGALES
def build_legal(p):
    toc = "\n".join(f'          <li><a href="#{i}">{t}</a></li>' for i, t in p["toc"])
    html = head(f'{p["title"]} | {BRAND}', p["meta"], f'{p["slug"]}.html')
    html += f"""<body>
{NAV}
<main id="contenido">

  <section class="page-head">
    <div class="wrap">
{breadcrumb(p["title"])}
      <h1 class="page-head__title">{p["title"]}</h1>
      <p class="page-head__lede">{p["lede"]}</p>
      <p class="page-head__meta">Última actualización: <time datetime="2026-08-12">12 de agosto de 2026</time></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{DRAFT}
      <div class="legal-layout">
        <aside class="legal-toc" aria-label="Contenido de la página">
          <h2>En esta página</h2>
          <ol>
{toc}
          </ol>
        </aside>

        <div class="prose">
{p["body"].strip()}
        </div>
      </div>
    </div>
  </section>

</main>

{footer(SERVICIOS)}
{breadcrumb_jsonld(p["title"], p["slug"])}
{COOKIE_BANNER}"""
    return write(f'{p["slug"]}.html', html)


# -------------------------------------------------------------- SERVICIOS
def build_service(s):
    badges = "\n".join(f"          <li>{b}</li>" for b in s["badges"])
    facts = "\n".join(
        f"""        <div class="fact">
          <span class="fact__num">{n}</span>
          <span class="fact__label">{l}</span>
        </div>""" for n, l in s["facts"])
    steps = "\n".join(
        f"""        <article class="step-card">
          <span class="step-card__num">Paso {i+1:02d}</span>
          <h3>{t}</h3>
          <p>{d}</p>
        </article>""" for i, (t, d) in enumerate(s["steps"]))

    note = ""
    if s.get("note"):
        nt, paras = s["note"]
        ps = "\n".join(f"        <p>{x}</p>" for x in paras)
        note = f"""
      <div class="clinical-note">
        <h3>{nt}</h3>
{ps}
      </div>"""

    rel = "\n".join(
        f"""        <a class="related__card" href="{SVC_BY_SLUG[r]['slug']}.html">
          <strong>{SVC_BY_SLUG[r]['nav']}</strong>
          <span>{SVC_BY_SLUG[r]['lede'][:78].rsplit(' ', 1)[0]}…</span>
        </a>""" for r in s["related"])

    cta_t, cta_x = s["cta"]

    html = head(s["title"], s["meta"], f'{s["slug"]}.html')
    html += f"""<body>
{NAV}
<main id="contenido">

  <section class="page-head page-head--service">
    <div class="wrap">
{breadcrumb(s["nav"])}
      <div class="page-head__grid">
        <div>
          <h1 class="page-head__title">{s["h1"]}</h1>
          <p class="page-head__lede">{s["lede"]}</p>
          <ul class="page-head__badges">
{badges}
          </ul>
          <div class="page-head__cta">
            <a class="btn btn--solid btn--lg" href="index.html#contacto">Pedir cita</a>
            <a class="btn btn--outline btn--lg" href="tel:{TEL_HREF}">Llamar · {TEL_TXT}</a>
          </div>
        </div>
        <figure class="page-head__figure">
          <picture>
            <source type="image/webp" srcset="{s["img"]}.webp">
            <img src="{s["img"]}.jpg" width="900" height="1120" decoding="async" alt="{s["alt"]}">
          </picture>
        </figure>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="fact-grid">
{facts}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <header class="section__head">
        <p class="eyebrow">Cómo lo hacemos</p>
        <h2 class="section__title">Paso a paso, sin letra pequeña</h2>
      </header>
      <div class="step-cards">
{steps}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="prose">
{s["body"].strip()}
      </div>{note}
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <header class="section__head">
        <p class="eyebrow">Preguntas</p>
        <h2 class="section__title">Lo que más nos preguntáis</h2>
      </header>
      <div class="faq__list">
{qa(s["faqs"])}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <header class="section__head">
        <p class="eyebrow">Otros servicios</p>
        <h2 class="section__title">Relacionado con este</h2>
      </header>
      <div class="related__grid">
{rel}
      </div>
    </div>
  </section>

{page_cta(cta_t, cta_x)}
</main>

{footer(SERVICIOS)}
{service_jsonld(s)}
{faq_jsonld(s["faqs"])}
{breadcrumb_jsonld(s["nav"], s["slug"])}
{COOKIE_BANNER}"""
    return write(f'{s["slug"]}.html', html)


# ----------------------------------------------------------------- GUÍAS
def build_guia(g):
    toc = "\n".join(f'          <li><a href="#{i}">{t}</a></li>' for i, t in g["toc"])
    cta_t, cta_x = g["cta"]
    html = head(g["title"], g["meta"], f'{g["slug"]}.html')
    html += f"""<body>
{NAV}
<main id="contenido">

  <section class="page-head">
    <div class="wrap">
{breadcrumb(g["h1"])}
      <h1 class="page-head__title">{g["h1"]}</h1>
      <p class="page-head__lede">{g["lede"]}</p>
      <p class="page-head__meta">Guía informativa · actualizada el <time datetime="{g["updated"]}">{g["updated_txt"]}</time></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="legal-layout">
        <aside class="legal-toc" aria-label="Contenido de la página">
          <h2>En esta página</h2>
          <ol>
{toc}
          </ol>
        </aside>

        <div class="prose">
{g["body"].strip()}
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0" id="preguntas">
    <div class="wrap">
      <header class="section__head">
        <p class="eyebrow">Preguntas</p>
        <h2 class="section__title">Preguntas frecuentes sobre veterinarias en Madrid</h2>
      </header>
      <div class="faq__list">
{qa(g["faqs"])}
      </div>
    </div>
  </section>

{page_cta(cta_t, cta_x)}
</main>

{footer(SERVICIOS)}
{article_jsonld(g)}
{faq_jsonld(g["faqs"])}
{breadcrumb_jsonld(g["h1"], g["slug"])}
{COOKIE_BANNER}"""
    return write(f'{g["slug"]}.html', html)


if __name__ == "__main__":
    done = [build_legal(p) for p in LEGALES]
    done += [build_service(s) for s in SERVICIOS]
    done += [build_guia(g) for g in GUIAS]
    for d in done:
        print("  OK", d)
    print(f"\n{len(done)} páginas generadas.")
