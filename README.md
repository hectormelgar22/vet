# Clínica veterinaria · Landing (Madrid)

Landing de una sola página para clínica veterinaria con urgencias 24 h.
HTML + CSS nativo + GSAP 3.13 (por CDN, con versión fijada). Sin build, sin
dependencias que instalar.

```bash
python -m http.server 5173
```

Luego abre `http://localhost:5173`.

---

## 1. Qué hay dentro

```
index.html                 Página completa (head, schema, secciones, banner)
aviso-legal.html           Aviso legal (LSSI-CE)
privacidad.html            Política de privacidad (RGPD / LOPDGDD)
cookies.html               Política de cookies (guía AEPD)
servicio-*.html            7 páginas de detalle, una por servicio
guia-veterinaria-madrid.html  Guía SEO: cómo elegir veterinaria en Madrid (blog)
calendario-mascota.html    Herramienta: calendario de vacunas y revisiones
consultor-toxicos.html     Herramienta: ¿puede comer esto?
calculadora-nutricion.html Herramienta: ración diaria y peso ideal
.build/                    Generador de las páginas interiores (python .build/build.py)
experiencia.html           Prototipo aparte: scroll cinematográfico (ver nota)
historias.html             Prototipo aparte: galería con zoom en perspectiva
assets/css/styles.css      Sistema de diseño y todos los componentes
assets/css/marquee.css     Carrusel de reseñas (compartido por index e historias)
assets/css/services.css    Lista de servicios con banda deslizante + imagen
assets/css/page.css        Páginas interiores (legales y detalle de servicio)
assets/css/team-flip.css   Tarjetas 3D del equipo (foto delante, cita detrás)
assets/css/experiencia.css Estilos del prototipo inmersivo
assets/css/historias.css   Estilos del prototipo de galería
assets/js/main.js          Navegación, hero animado, triaje, opiniones, formulario
assets/js/services.js      Lista de servicios: banda, imagen y descripción sincronizadas
assets/js/page.js          Navegación de las páginas interiores (sin GSAP)
assets/js/team-flip.js     Interacción de las tarjetas del equipo (hover/toque/teclado)
assets/js/experiencia.js   Scroll cinematográfico del prototipo (Lenis)
assets/js/historias.js     Zoom en perspectiva del prototipo (ScrollSmoother)
assets/js/cookies.js       Banner y Consent Mode v2
assets/img/                Imágenes de relleno (.webp + .jpg) y grano (grain.png)
assets/img/galeria/        12 fotos de mascota (Unsplash) para el collage
assets/img/servicios/      7 fotos (Unsplash), una por servicio
assets/video/              Vídeos del hero y de la experiencia
.claude/launch.json        Servidor local para previsualizar
```

Secciones de `index.html`: cabecera flotante → **hero cinematográfico** →
cifras → triaje → servicios → tu visita paso a paso → instalaciones →
**opiniones con collage en zoom + carrusel** → equipo → **herramientas** →
banda de urgencias → preguntas frecuentes → contacto → pie → barra fija móvil.

### Dos fallos serios que estaban en producción

**1. Al hacer zoom (Ctrl +/−) las fotos de opiniones aparecían de golpe.**
La causa era `html { scroll-behavior: smooth }` en el CSS. Cuando ScrollTrigger
recalcula medidas —y un cambio de zoom se lo dispara— lleva el scroll a 0 para
medir las posiciones naturales y luego lo restaura. Con `scroll-behavior:
smooth`, ese salto lo **anima** el navegador en vez de aplicarlo al instante,
así que GSAP medía creyendo estar en 0 mientras la página seguía desplazada:
todos los triggers quedaban corridos exactamente `-scrollY`. Medido: el collage
declaraba empezar en el píxel 93 cuando estaba en el 9036, con lo que el
progreso saltaba a 1 y todo se mostraba en su estado final.

Es una incompatibilidad conocida y documentada de GSAP. Se ha quitado del CSS y
el desplazamiento suave de los enlaces internos lo hace ahora `main.js`, que
solo suaviza el clic del usuario y no interfiere con las medidas.

**2. En móvil no se podía abrir el menú.** La marca de la píldora llevaba
`flex: none` y medía 249 px; sumada a las acciones (165 px) desbordaba la
píldora de 351 px, y el botón de la hamburguesa quedaba **fuera de pantalla**
(x 415–461 en un viewport de 375). Ahora la marca puede encogerse y cede el
texto por debajo de 700 px (subtítulo) y de 540 px (nombre completo), quedando
el logotipo, que también lleva a inicio. Verificado: hamburguesa en 306–352,
46×46 px, menú abriendo con sus seis enlaces.

También se corrigió que la tabla de la política de cookies (560 px) desbordara
la página en móvil: era el `min-width: auto` que traen por defecto los
elementos de rejilla, que impedía al contenedor encoger y activar su scroll.

### Páginas interiores

Diez páginas nuevas, generadas desde `.build/` para que compartan cabecera,
píldora y pie: si cambia la identidad, se toca el generador y se reconstruye con
`python .build/build.py`.

- **Legales** (`aviso-legal`, `privacidad`, `cookies`): estructuradas sobre la
  LSSI-CE, el RGPD, la LOPDGDD y las guías de la AEPD. La de cookies describe
  **lo que la web hace de verdad**, comprobado en el código: solo guarda
  `vc_consent_v2` en almacenamiento local, con todo denegado por defecto, sin
  mapa incrustado ni píxeles.
- **Servicios** (7): cómo se trabaja paso a paso, qué se resuelve en la propia
  clínica, cuándo se deriva, avisos clínicos y preguntas frecuentes. Llevan
  JSON-LD de `Service`, `FAQPage` y `BreadcrumbList`.

Desde la home se accede pinchando en el nombre del servicio o en la flecha, que
apunta siempre al servicio que se está previsualizando.

> **Los textos legales son un punto de partida, no un documento listo.** Los
> datos que solo puede aportar la clínica (CIF, datos registrales, hosting,
> DPD) van marcados como `COMPLETAR` y **se ven en la página a propósito**, para
> que nadie la publique por descuido creyéndola terminada. Cada página lleva
> además un aviso visible. No son asesoramiento jurídico y conviene que los
> revise un profesional.

### Seguridad y rendimiento

- **SRI en los 11 scripts de CDN** (`integrity` + `crossorigin` +
  `referrerpolicy`). Si jsDelivr se viera comprometido y sirviera un GSAP
  alterado, el navegador lo bloquearía en vez de ejecutarlo. Verificado que los
  hashes son correctos: con uno mal, el script no cargaría.
- Versiones de GSAP unificadas en 3.13.0 en las tres páginas que lo usan.
- `preconnect` al CDN, `fetchpriority="high"` en la imagen de cabecera de las
  páginas de servicio (que es su LCP) y `loading="lazy"` en la de servicios de
  la home, que está bajo el pliegue.
- Las páginas interiores **no cargan GSAP** ni `main.js`: usan `page.js`, que
  solo trae la navegación.
- `ScrollTrigger.config({ ignoreMobileResize: true })`: en móvil, mostrar u
  ocultar la barra del navegador cambia la altura del viewport y disparaba
  refrescos constantes.

Pendiente y anotado: las páginas interiores cargan `styles.css` entero (49 KB
sin comprimir), del que usan poco más de la mitad. Separar el sistema de diseño
del CSS de la home ahorraría algunos KB, pero es un refactor con riesgo de
regresión y comprimido son ~12 KB.

### Sección de peluquería en la home

Entre **servicios** y **tu visita** hay una sección (`#peluqueria`) de
peluquería canina y felina. Reutiliza la rejilla de fotos de Instalaciones
(`.facilities__grid` / `.shot`), con una foto grande de perro y dos pequeñas
(gato y secado). El texto la plantea como salud, no solo estética: en cada
sesión se revisan piel, oídos y uñas. La barra de navegación incluye su
enlace; con ocho secciones, los enlaces en línea aparecen a partir de 1200 px
(por debajo, menú desplegable) y el botón de urgencias solo a partir de
1440 px, para que nunca se apretujen ni se parta ninguno en dos líneas.

### Guía SEO (`guia-veterinaria-madrid.html`)

Artículo de contenido (tipo blog) generado por `.build/build.py` con la misma
cabecera, pie y layout que las páginas legales (TOC lateral + `.prose`). El
texto es divulgativo, no clínico, así que no necesita firma colegiada. Lo que
le da valor SEO no es el texto en sí (genérico) sino: `<title>` y
`meta description` propios, **datos estructurados** `Article` + `FAQPage` +
`BreadcrumbList` (candidato a resultados enriquecidos), y **enlazado interno**
a las siete páginas de servicio y a las tres herramientas. Se enlaza desde el
pie de todas las páginas (columna «Clínica»).

Aviso: la cifra del censo («más de 300.000 perros») está marcada en
`.build/guias.py` como pendiente de verificar contra la fuente municipal antes
de publicarla como dato. Un artículo por sí solo no posiciona: el SEO local
depende sobre todo de la ficha de Google Business, reseñas reales y un NAP
coherente.

### Sección de herramientas en la home

Entre **equipo** y la banda de urgencias hay una sección (`#herramientas`) con
tres tarjetas que enlazan a las utilidades. El orden es deliberado: equipo
(cálido) → herramientas (útil) → urgencias (llamada a la acción) → preguntas.
La tarjeta del consultor de tóxicos lleva el acento ámbar/brasa porque es la
que se abre con una urgencia entre manos; las otras dos, el verde de la marca.

### Tres herramientas para el visitante

Son **archivos únicos autocontenidos**: cada uno lleva su HTML, su CSS y su JS
dentro, sin más dependencia externa que Google Fonts. No comparten `styles.css`
a propósito, para que se puedan mover, enlazar o incrustar sin arrastrar el
resto del sitio. Usan los mismos tokens de color y tipografía, así que se ven
nativas. **Ninguna guarda nada en el navegador ni envía datos a ningún sitio.**

| Archivo | Qué hace |
|---|---|
| `calendario-mascota.html` | Formulario de 3 pasos → línea temporal de vacunas, desparasitaciones y revisiones, con estados (hecho / toca ahora / atrasado / futuro / periódico) y hoja de impresión limpia. |
| `consultor-toxicos.html` | Buscador «¿puede comer esto?» con semáforo, síntomas, latencia y pasos a seguir. Barra de urgencia fija cuando el resultado es rojo. |
| `calculadora-nutricion.html` | Ración diaria orientativa, rango de peso ideal por raza y escala de condición corporal 1-9 con siluetas SVG paramétricas. |

#### Qué está verificado y qué no

Esto es lo más importante de las tres herramientas:

- **Las fórmulas de la calculadora son estándar y públicas**: RER = 70 × kg^0,75
  y MER = RER × factor. Eso es matemática publicada. Verificado contra un
  cálculo independiente: un labrador de 40 kg da 495 g, coincide al gramo.
- **Los protocolos del calendario son 100 % de ejemplo.** Los calendarios
  vacunales varían por país, comunidad, laboratorio y animal: no hay una
  respuesta única que se pueda escribir sin la clínica. Todo el array
  `PROTOCOLO` va marcado `// VERIFICAR CON LA CLÍNICA`.
- **El diccionario de tóxicos recoge consenso veterinario establecido**
  (chocolate, xilitol, uva, *Allium*…), pero **todas** las fichas van marcadas
  para revisión colegiada, no solo las cinco plantillas vacías: las latencias y
  las gradaciones de gravedad varían entre fuentes. Cada ficha muestra en
  pantalla que está pendiente de revisión.
- **En ningún sitio se dan dosis, umbrales ni remedios caseros**, y el consultor
  dice explícitamente que no se induzca el vómito.
- Los **rangos de peso por raza** y los **multiplicadores energéticos** van
  marcados `// VERIFICAR`.

#### Decisiones de diseño que costaron una corrección

- **El calendario generaba 304 hitos** en su primera versión: un antiparasitario
  mensual son 180 entradas en 15 años. Peor aún, un gato de ocho años salía con
  **155 hitos «atrasados»**, es decir, le decía al dueño que llevaba 155
  tratamientos sin poner.

  La solución definitiva: **lo que se repite aparece UNA sola vez**, con su
  cadencia («Cada mes», «Cada 3 meses») y su próxima fecha, en un estado visual
  propio —`recurrente`— que no es ni «hecho» ni «atrasado», porque un
  tratamiento de por vida no es ninguna de las dos cosas. Un perro adulto pasó
  de 51 tarjetas a 6, y un gato de 12 años a 5. La casilla del paso 3 sigue
  siendo útil para ellos: marcarla significa «se lo he puesto hace poco» y
  recalcula la próxima fecha desde hoy en vez de desde la pauta teórica.

  Al hacerlo apareció un fallo derivado: la «próxima cita recomendada» solo
  miraba los estados antiguos, así que un animal adulto —cuyos hitos son todos
  periódicos— mostraba «Sin hitos pendientes» teniendo cinco por delante.
  Corregido.
- **El consultor se quedaba mudo** al buscar algo que no está en el diccionario:
  ni sugerencias ni aviso. En una herramienta que se usa de madrugada y con
  prisa, eso parece que la app se ha colgado. Ahora avisa en el acto y ofrece el
  teléfono.
- **La calculadora se contradecía**: la barra decía «sobrepeso» mientras la
  escala corporal marcaba 8, que es «obesidad». Medía el desvío contra el punto
  medio del rango y las zonas contra el máximo. Ahora ambas usan la misma
  referencia (el rango de la raza) y coinciden siempre.
- Con **mestizo o raza fuera de lista**, la calculadora **no inventa un
  veredicto** de peso: dice que sin rango de referencia eso se valora en
  consulta, y calcula solo la ración.

### Servicios: lista con banda deslizante

Al pasar por cada servicio (o tocarlo, o llegar con el tabulador) cambian a la
vez la foto, la descripción y el pie de imagen. Una banda verde se desliza de
fila en fila marcando cuál está activa.

**La banda, y por qué no usa `mix-blend-mode`.** El montaje de partida pintaba
una banda blanca con `mix-blend-mode: difference`: invierte "gratis" lo que
cubre, y por eso el texto de la fila activa se vuelve claro solo. Es ingenioso,
pero el color que sale es el que dicte la resta de canales — no se elige, y por
tanto **no se puede verificar el contraste**, que en esta web se comprueba
sección por sección.

Aquí se consigue el mismo efecto con control total: la banda es verde pino y
lleva dentro una **copia de las filas en color claro**, recortada por la propia
banda (`overflow: hidden`). Donde está la banda se ve la copia clara; fuera,
las filas normales. La copia se genera clonando el DOM en JS —una sola fuente
de verdad para los nombres— y se contra-desplaza en el eje Y con el mismo
`ease` y la misma duración que la banda, de modo que su texto cae exactamente
sobre el de las filas reales. Verificado: 0 px de desfase en las 7 filas, y las
8 combinaciones de color pasan AA.

> Cuidado al retocar la entrada: filas reales y copia tienen que animarse
> **emparejadas** (mismo `stagger` por índice). Si solo se animan las reales,
> durante la entrada la copia queda desplazada y se ve el texto duplicado.

Otras diferencias con el original: los textos de los siete servicios están en
el HTML (no en un array de JS), así que Google los indexa y la sección se lee
entera aunque el script no cargue; y las imágenes de los demás servicios no se
piden hasta que la sección entra en pantalla.

Se conserva del original el detalle más fino: el **hover que también funciona
mientras se hace scroll**. El navegador no dispara eventos de hover cuando la
página se mueve bajo un cursor quieto, así que se guarda la posición del
puntero y se comprueba qué hay debajo también en cada scroll (con `rAF` para no
medir de más).

Con `prefers-reduced-motion` la sección se convierte en una lista completa de
los siete servicios con su descripción, sin selector ni animación.

### Equipo: tarjetas 3D con peso

Foto y puesto delante, cita y colegiado detrás. Se abren al pasar el ratón, al
tocar o con el tabulador; solo una a la vez y `Escape` las cierra todas.

Lo que las diferencia de un flip corriente es que **no giran planas**:

- **Arco de elevación.** A mitad del giro la tarjeta avanza ~90 px hacia el
  espectador y vuelve a asentarse. Un giro de 180° sin ese arco se lee como un
  naipe de cartón; con él, como un objeto con grosor.
- **La sombra acompaña**: se separa y se abre mientras la tarjeta está en el
  aire (0,3 → 0,5 de opacidad), y vuelve al posarse.
- **Inclinación con el cursor**: la tarjeta se ladea hasta 7° siguiendo al
  ratón.
- **El reverso se compone** tras cruzar los 90°, escalonando epígrafe, cita y
  firma, en vez de aparecer de golpe.

Todo esto obliga a **tres capas anidadas** (`.flip-card` → `__tilt` →
`__inner`): la inclinación y el giro no pueden vivir en el mismo `transform`
sin pisarse. La elevación va en la capa de inclinación y el giro en la interna.

Sobre el color: el acento de cada tarjeta (pino, musgo, ámbar) va en el punto,
el canto y el tinte del velo — **nunca en el texto**. Como texto sobre tinta,
el pino da 1,39:1 y el musgo 3,41:1, muy por debajo del mínimo AA; los
epígrafes usan siempre el tono neutro (9,17:1) y, en la cara de la foto, una
píldora de cristal propia para no depender de lo que haya en la imagen.

### La barra: una píldora flotante que no molesta

En vez de una franja fija de ancho completo (que tapaba los momentos
inmersivos: el vídeo a pantalla completa y el zoom de opiniones), la navegación
es una **píldora flotante** (`.nav`, `position: fixed`) con fondo glass propio,
por lo que se lee sobre cualquier sección, clara u oscura. Comportamiento:

- Flota siempre a 18px del borde. **Ya no hay barra verde de aviso**: ocupaba
  espacio arriba y empujaba el titular del hero contra la píldora. El teléfono
  y el «Urgencias 24 h» que llevaba se mudaron dentro de la propia píldora
  (visibles a partir de 1200px; por debajo quedan en el desplegable y en la
  barra fija de móvil, así que no se pierde la llamada a un toque).
- **Se esconde al bajar y reaparece al instante al subir**: durante la lectura
  inmersiva desaparece, y basta un gesto hacia arriba para recuperarla. El logo
  queda siempre a un movimiento de distancia.
- En pantallas anchas (≥1040px) los enlaces van dentro de la píldora; por
  debajo, se pliegan en un desplegable bajo el botón hamburguesa. (Antes, en
  escritorio, no se veían los enlaces: solo salían en el desplegable.)
- Con `prefers-reduced-motion` no se auto-oculta: se queda siempre visible.
- `scroll-padding-top: 96px` deja que, al pulsar un enlace, el encabezado de la
  sección caiga por debajo de la píldora y no quede tapado.

### Opiniones: el zoom sale de escena, no se corta

El collage no se limita a acercarse: la línea de tiempo tiene **tres actos**
dentro de un mismo pin (`+=230%`).

1. **Entrada (0 → 0.55).** Las fotos avanzan en Z y el titular emerge desde el
   fondo.
2. **Respiro (0.55 → 0.68).** Todo se detiene un momento: el titular se lee
   solo, sin competir con el movimiento.
3. **Salida (0.68 → 1).** Las fotos siguen creciendo y pasan de largo mientras
   se desvanecen, escalonadas por capas; el titular las sigue con un
   desenfoque. El lienzo queda limpio **antes** de que entre el carrusel, que
   sube con un fundido y sus tarjetas escalonadas.

Antes solo existía el acto 1: la animación se cortaba en seco a pleno zoom y el
carrusel entraba encima, que es lo que se veía «con pinzas».

> **Cuidado si se retoca la salida.** El acto 3 agranda con `scale`, no con más
> `z`. La `perspective` es `100svh`, así que en cuanto `z` supera el alto de la
> ventana el elemento cruza el plano de la cámara y la proyección se invierte:
> las fotos, en vez de seguir creciendo, encogen de golpe. Con `scale` el
> efecto es idéntico y no depende del tamaño de la ventana.

El carrusel de abajo es CSS puro (`assets/css/marquee.css`, sin GSAP): se
duplica la lista de tarjetas y se anima `translateX(-50%)` → `translateX(0%)`;
como el segundo bloque es idéntico al primero, el salto al reiniciar es
invisible. Ese segundo bloque lleva `aria-hidden="true"` para que un lector de
pantalla no lea las reseñas dos veces. Se pausa al pasar el ratón y, con
`prefers-reduced-motion`, se detiene y pasa a ser una fila deslizable a mano.
Las 4 reseñas van con el texto íntegro, el mismo que declara el JSON-LD.

### Motion en el resto de la página

- **Revelados en lote** (`ScrollTrigger.batch`) en vez de uno a uno: lo que
  entra junto en pantalla se escalona entre sí.
- **Encabezados de sección** en cascada corta (epígrafe → título → entradilla).
- **Parallax** en las fotos de instalaciones. Se anima el `<picture>`, **no la
  `<img>`**: el zoom al pasar el ratón es CSS sobre la `img`, y si GSAP le
  escribiera `transform` en línea lo anularía. (El equipo ya no lo lleva: sus
  tarjetas tienen su propio movimiento 3D y pelearían por el mismo `transform`.)
- **Numeración de «Tu visita»**, banda de urgencias y contadores de cifras con
  entradas propias.
- **Micro-interacciones**: el pie de foto de instalaciones se asoma, los
  enlaces del menú se asientan, las tarjetas de reseña se elevan. Todas son
  `transform`/`opacity` y se apagan con `prefers-reduced-motion`.

### El hero, en dos tiempos

1. **El mensaje.** Pantalla completa centrada con el `<h1>`, el texto, los dos
   botones y los tres motivos de confianza. Al empezar a bajar, el bloque gira
   sobre su eje X y se desvanece, como un rollo de película.
2. **El vídeo.** Arranca como un marco pequeño y crece hasta ocupar
   `94vw × 90svh` mientras se descubre el mensaje «Tiempo para cada paciente».
   La tarjeta de valoración (4,9/5) se mantiene encima.

El `<h1>` y los CTA siguen en la primera pantalla a propósito: es una landing
de captación, no una pieza de portfolio, y esconder el «Pedir cita» tras 250vh
de scroll costaría citas.

### Por qué en la home no hay Lenis ni ScrollSmoother

Los prototipos usan motores de scroll suave: `experiencia.html` usa **Lenis** e
`historias.html` usa **ScrollSmoother**. Son incompatibles entre sí (dos
motores peleándose por el scroll), y ScrollSmoother además envuelve la página
en un contenedor `position: fixed`, lo que rompería la cabecera flotante, la
barra fija de móvil y el banner de cookies.

Por eso en `index.html` los dos efectos están portados a **ScrollTrigger a
secas** (pin + scrub), que ya estaba en la página. Se pierde el suavizado del
scroll, pero se gana no tocar la estructura ni romper nada de lo que ya
funcionaba, y el scroll nativo va mejor en móvil.

### Los dos prototipos siguen ahí

`experiencia.html` e `historias.html` se quedan en el repo como prototipos
navegables (y como referencia de los efectos originales), pero **ya no se
enlazan desde el menú**: su contenido vive ahora en el hero y en opiniones, y
tener dos rutas que enseñan lo mismo confunde. Si no se van a usar, se pueden
borrar junto con sus `.css`/`.js`; el único archivo compartido es
`marquee.css`, que sí usa la home.

---

## 2. Decisiones de diseño

**El hero da la bienvenida, no alarma.** Fondo claro y cálido (crema → menta
con un halo de luz dorada), titular «Tu veterinario de _confianza_ en Madrid»
—que mantiene el «Veterinario en Madrid» para el SEO local— y un vídeo de una
mascota recibiendo caricias, con una tarjeta de valoración («4,9/5 · 187
familias contentas»). Transmite cercanía y confianza en lugar de urgencia. La
reassurance de las 24 h sigue presente, pero como «aquí estamos», no como
drama. El vídeo va sobre fondo claro, en el lado derecho, para que el texto se
lea sin capas oscuras encima.

**El elemento firma es el triaje.** Justo debajo del hero, quien tiene una
urgencia real quiere saber si debe salir de casa ahora. El bloque «¿Qué le
pasa?» combina especie + síntoma y devuelve una recomendación con nivel de
urgencia, servicio y acción. Siete motivos × tres especies, con matices
clínicos reales donde la especie cambia el consejo (lipidosis hepática en
gatos, torsión gástrica en perros grandes, estasis digestiva en conejos).

**Paleta.** Verde bosque (`#0F3D36`) como color de marca y de confianza, lino
cálido (`#F4F6F2`), un ámbar suave (`#E8B04B`) para el brillo amable y un acento
brasa (`#E4572E`) reservado a lo verdaderamente urgente (banda de urgencias,
alertas). Se evita a propósito el turquesa-naranja que llevan casi todas las
webs veterinarias.

**Tipografía.** Fraunces para titulares (serif variable, con eje SOFT alto:
cálida y cercana, no fría), Figtree para texto e IBM Plex Mono para etiquetas y
horarios.

**Movimiento.** Una sola secuencia de entrada en el hero (texto escalonado +
el marco del vídeo asentándose), revelados cortos al hacer scroll y un parallax
mínimo. Todo con `transform` y `opacity`. Se apaga entero con
`prefers-reduced-motion`.

**Vídeo del hero.** Clip de stock de [Mixkit](https://mixkit.co) («dog being
petted»), bajo licencia Mixkit —uso comercial gratuito, sin atribución
obligatoria—. Se sirve en dos tamaños: `hero-720.mp4` (4,4 MB) en escritorio y
`hero-360.mp4` (0,9 MB) en móvil. Carga condicionada por JavaScript: si el
usuario tiene activado «reducir movimiento» o el ahorro de datos, se queda el
póster estático y el vídeo ni se descarga. Sustitúyelo por un vídeo propio de
la clínica cuando lo tengas (mismo nombre de archivo y listo).

---

## 3. Identidad de muestra — hay que sustituirla al firmar un cliente real

La maqueta usa una identidad ficticia completa para poder enseñarse y
auditarse como una web terminada, no como una plantilla a medio rellenar:

- **Nombre:** Clínica Veterinaria Vitalis
- **Dirección:** Calle de Alcalá, 415, 28027 Madrid (coordenadas orientativas)
- **Teléfono:** 910 305 305 · **Email:** citas@vitalisveterinaria.es
- **Dominio de referencia:** vitalisveterinaria.es
- **Equipo:** Elena Marín (dirección clínica), Rubén Castillo (cirugía),
  Irene Palop (anestesia/hospitalización), con números de colegiado
  inventados con formato válido del Colegio de Veterinarios de Madrid
- **Testimonios y `aggregateRating`** (4,9/5, 187 reseñas) en el JSON-LD,
  con el mismo texto que se ve en la página

**Nada de esto es real.** En cuanto haya un cliente real, hay que sustituir
absolutamente todo lo anterior por sus datos reales antes de publicar el
dominio: un NAP inventado en producción daña el Local Pack, y publicar
valoraciones inventadas como si fueran reales incumple las políticas de
Google (spam de fragmentos enriquecidos) y puede acarrear una acción manual
sobre el dominio real. Busca `IDENTIDAD DE MUESTRA` en `index.html:91` para
el aviso completo.

| Dónde | Qué sustituir |
|---|---|
| `index.html` `<head>` | `G-XXXXXXXXXX` por el ID real de GA4 y descomentar el bloque (no es inventable: tiene que ser una propiedad real) |
| JSON-LD | Nombre, dirección, teléfono, email, `geo`, `sameAs`, equipo y colegiados |
| JSON-LD | `aggregateRating` y `review`: por reseñas reales, con el mismo texto visible en la página |
| Todo el HTML | `+34910305305` y `910 305 305` |
| Sección equipo | Retratos reales (ahora mismo son ilustraciones generadas) |
| Pie | Nº de registro de centro veterinario y dirección técnica |
| Enlaces legales | Aviso legal, privacidad y cookies (ahora apuntan a `#`) |
| `assets/img/` | Retratos del equipo y avatares son ilustraciones generadas; sustituir por fotos reales en WebP |
| `assets/img/instalacion-*` | Fotos de stock (no son la clínica real); ver nota abajo |
| `assets/img/peluqueria-*` | Fotos de stock de la peluquería (no son las reales); ver nota abajo |
| `assets/video/` | Vídeo de stock de Mixkit; sustituir por uno propio de la clínica (mismo nombre) |
| `main.js` | Constante `TEL` |

### Un aviso que conviene no saltarse

El mapa de Google no está incrustado. Un `iframe` de Maps escribe cookies de
terceros antes del consentimiento. En su lugar hay un bloque que abre el
panel de cookies; cuando lo conectes, cárgalo solo tras aceptar.

### Fotos de Instalaciones y Peluquería: son de stock, no de esta clínica

Las tres fotos de **Instalaciones** (`instalacion-recepcion`,
`instalacion-sala`, `instalacion-espera`) y las tres de **Peluquería**
(`peluqueria-perro`, `peluqueria-gato`, `peluqueria-secado`) son fotos de
banco (Pexels, licencia libre y uso comercial), cada trío de la misma sesión
para que combinen entre sí. **No son la clínica del cliente.**

Las de Instalaciones se eligieron a propósito para que muestren el **espacio**
(salas de consulta amplias, equipo, ambiente) y no primeros planos de un
procedimiento: la sección responde a «cómo es la clínica por dentro», no a
«qué hacemos». Las anteriores (`instalacion-quirofano/hospital/consulta`) eran
macros de una ecografía y una inyección, que no daban esa idea de sitio; se
sustituyeron. Sustituir todas por fotos reales de la clínica en cuanto se
pueda — es lo primero que un cliente real debería cambiar, junto con el equipo.

---

## 4. Privacidad y formulario

- **Consent Mode v2** declarado en el `<head>`, antes de cualquier etiqueta:
  `ad_storage`, `ad_user_data`, `ad_personalization` y `analytics_storage` en
  `denied`; `functionality_storage` y `security_storage` en `granted`.
  `ads_data_redaction` activo y `wait_for_update: 500`.
- **Banner** con «Rechazar todo» y «Aceptar todo» de idéntico tamaño, peso,
  color y posición. `Esc` equivale a rechazar. La decisión se guarda con fecha
  y caduca a los 180 días. Reabrible desde el pie.
- **Honeypot**: campo `website` fuera de pantalla (no `display:none`, que
  algunos bots detectan), con `tabindex="-1"` y `autocomplete="off"`. Si llega
  relleno, el envío se descarta en silencio. Se añade un control de tiempo:
  menos de 3 segundos entre carga y envío se considera automatizado.
- **Consentimiento explícito** desmarcado por defecto, separado del check
  comercial (que es opcional), con adenda de confidencialidad clínica y vía
  para ejercer derechos.

> **Pendiente de backend.** La validación de cliente no es una barrera de
> seguridad. Al conectar el `POST`, repite en servidor la comprobación del
> honeypot, añade límite de peticiones por IP, valida y sanea todos los campos
> y registra el consentimiento (fecha, hora, IP y texto aceptado).

---

## 5. Verificaciones ejecutadas

Sobre la página renderizada en el navegador, no sobre el papel:

- **Contraste WCAG 2.1 AA**: auditoría automática de los 223 nodos de texto
  con color efectivo calculado sobre el fondo real compuesto (incluye capas
  translúcidas). **0 fallos.** Se corrigieron tres textos de la banda de
  urgencias: sobre el brasa `#E4572E` solo el tinta `#0B211E` alcanza 4,56:1;
  ningún marrón intermedio llega a 4,5.
- **Sin desbordamiento horizontal** a 375, 800 y 1440 px.
- **Objetivos táctiles**: botones, chips y campos ≥ 44 px; enlaces de pie y
  legales a 32 px (mínimo AA de WCAG 2.2 SC 2.5.8 es 24×24). Los que quedan
  por debajo son enlaces en línea dentro de una frase, exentos por la norma.
- **Hero nuevo (claro)**: auditoría de contraste del hero y la tarjeta de
  valoración → **0 fallos**. Título en tinta verde sobre fondo claro,
  «confianza» en verde musgo, botón «Pedir cita» verde pino con blanco (12:1).
- **Estructura**: un solo `<h1>` («…Veterinario…en Madrid»), `<h2>` por
  sección de servicio, sin saltos de nivel, landmarks completos, `lang="es"`.
- **JSON-LD**: parsea correctamente y expone `VeterinaryCare` (con
  `aggregateRating` y `review`), `WebSite` y `FAQPage`.
- **Vídeo del hero**: en escritorio carga `hero-720.mp4` (1280×720) y en móvil
  `hero-360.mp4` (640×360); reproduce en bucle, silenciado. Con «reducir
  movimiento» o ahorro de datos se queda el póster.
- **Imágenes**: las rutas WebP responden y el navegador elige WebP sobre el
  respaldo JPG. Todo lo que está bajo el primer pliegue lleva `loading="lazy"`
  y `width`/`height` para no provocar saltos de maquetación.
- **Funcional**: triaje (21 combinaciones, `aria-pressed` correcto), envío
  vacío marca los 4 campos obligatorios, honeypot relleno descarta en
  silencio, envío válido confirma.
- **Degradación**: sin JavaScript o con la CDN de GSAP caída, la página se ve
  entera (el contenido solo se oculta si hay JS que pueda revelarlo).

Revisado visualmente a 375 y 1440 px con capturas: el hero se ve claro, cálido
y con el vídeo de la mascota en su marco; el resto de la página no cambió.
