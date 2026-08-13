# -*- coding: utf-8 -*-
"""Artículos / guías informativas (contenido SEO).

Cada guía es un dict con la misma forma que los servicios/legales, para que
`build.py` la ensamble con la misma cabecera, pie y banner de cookies. El texto
es divulgativo (orientado al dueño de la mascota), no clínico: no da pautas ni
dosis, así que no necesita firma colegiada como las herramientas. Enlaza a las
páginas de servicio y a las herramientas para reforzar el enlazado interno.
"""

# NOTA CLIENTE: verificar la cifra del censo antes de publicarla como dato con
# fuente. El Ayuntamiento de Madrid publica el censo de animales de compañía;
# la cifra exacta cambia cada año. Si no se puede citar con seguridad, cambiar
# "más de 300.000 perros censados" por "cientos de miles de perros".

GUIA_VETERINARIA = dict(
    slug="guia-veterinaria-madrid",
    title="Veterinaria de confianza en Madrid: guía para elegir bien | Clínica Veterinaria Vitalis",
    meta=("Guía para elegir veterinaria en Madrid: servicios esenciales, urgencias 24 h, "
          "medicina preventiva, diagnóstico avanzado y preguntas frecuentes sobre el cuidado animal."),
    h1="Tu veterinaria de confianza en Madrid para el cuidado animal",
    lede=("Qué distingue a una buena clínica veterinaria, qué servicios debe ofrecerte y "
          "cómo actuar cuando tu mascota más lo necesita."),
    updated="2026-08-13",
    updated_txt="13 de agosto de 2026",
    toc=[
        ("que-es", "Qué es una veterinaria de confianza"),
        ("servicios", "Servicios esenciales en Madrid"),
        ("elegir", "Cómo elegir la mejor"),
        ("urgencias", "Atención de urgencias"),
        ("preventiva", "Medicina preventiva"),
        ("tecnologia", "Tecnología y diagnóstico"),
        ("preguntas", "Preguntas frecuentes"),
        ("conclusion", "En resumen"),
    ],
    body="""
<p>
  Madrid es una ciudad de animales. Según el censo municipal de animales de compañía,
  más de 300.000 perros están registrados en la capital, y la cifra de gatos, conejos y
  otras mascotas sigue creciendo cada año. Con ese volumen de animales conviviendo en
  hogares madrileños, encontrar una veterinaria de confianza no es un detalle menor: es
  una de las decisiones más importantes que toma un dueño responsable. Esta guía está
  pensada para ayudarte a entender qué distingue a una buena clínica veterinaria, qué
  servicios debe ofrecerte y cómo actuar cuando tu mascota más lo necesita.
</p>

<h2 id="que-es">¿Qué es una veterinaria de confianza?</h2>
<p>
  Una clínica veterinaria de confianza no se define únicamente por su equipamiento o por
  su ubicación. Se define, sobre todo, por la relación que construye con el animal y con
  su dueño a lo largo del tiempo. Un centro de referencia cuenta con profesionales
  colegiados y con experiencia contrastada, ofrece información clara sobre diagnósticos y
  tratamientos, y trata a cada paciente —sea un golden retriever de doce años o un hámster
  recién llegado a casa— con el mismo rigor y la misma atención.
</p>
<p>
  Otros indicadores de confianza son la transparencia en los presupuestos, la
  disponibilidad para resolver dudas fuera de consulta y la capacidad de derivar a
  especialistas cuando el caso lo requiere. En una ciudad como Madrid, donde la oferta es
  amplia, los propietarios de mascotas valoran cada vez más estos factores junto a la
  cercanía geográfica.
</p>

<h2 id="servicios">Servicios veterinarios esenciales en Madrid</h2>
<p>
  Una clínica veterinaria completa debe cubrir, como mínimo, un núcleo de servicios
  básicos que garanticen el bienestar del animal en todas las etapas de su vida.
</p>
<p>
  Las <a href="servicio-consulta.html"><strong>consultas de medicina general</strong></a>
  son la puerta de entrada: revisiones anuales, diagnóstico de enfermedades comunes y
  seguimiento de patologías crónicas como la diabetes o la artritis. A estas se suman los
  programas de <a href="servicio-preventiva.html"><strong>vacunación</strong></a>,
  imprescindibles para proteger tanto al animal como al entorno humano frente a
  enfermedades como el moquillo, la rabia o la leucemia felina.
</p>
<p>
  La <a href="servicio-cirugia.html"><strong>cirugía veterinaria</strong></a> —desde
  esterilizaciones y extracciones dentales hasta intervenciones de mayor complejidad—
  requiere instalaciones adecuadas y personal especializado en
  <a href="servicio-anestesia.html">anestesiología animal</a>. Por último, el
  <a href="servicio-urgencias.html"><strong>servicio de urgencias</strong></a> es el que
  marca la diferencia en los momentos críticos: intoxicaciones, traumatismos o
  dificultades respiratorias no esperan al horario de apertura habitual.
</p>

<h2 id="elegir">Cómo elegir la mejor veterinaria en Madrid</h2>
<p>
  Con centenares de clínicas repartidas por los distritos de la capital, la elección puede
  resultar abrumadora. Hay cuatro criterios que conviene valorar con detenimiento.
</p>
<p>
  La <strong>ubicación y la accesibilidad</strong> importan más de lo que parece: llegar en
  diez minutos en caso de emergencia puede ser determinante. Los <strong>horarios
  amplios</strong>, incluidas mañanas de fin de semana, facilitan la conciliación y evitan
  que una consulta de rutina se convierta en un problema logístico.
</p>
<p>
  Las <strong>especialidades disponibles</strong> marcan la diferencia conforme el animal
  envejece o presenta problemas concretos: dermatología, oftalmología, oncología o
  traumatología veterinaria son servicios que no todas las clínicas ofrecen. Finalmente,
  las <strong>valoraciones de otros propietarios</strong> —en Google, en foros
  especializados o en grupos vecinales— aportan una perspectiva real sobre el trato, los
  tiempos de espera y la calidad de la comunicación con el equipo clínico.
</p>

<h2 id="urgencias">Atención veterinaria de urgencias en Madrid</h2>
<p>
  Ningún dueño de mascota está exento de vivir una emergencia. Una pelea con otro perro, la
  ingestión de un alimento tóxico o una caída desde altura son situaciones que pueden
  presentarse en cualquier momento, incluidas las madrugadas de un domingo festivo.
</p>
<p>
  Contar con una veterinaria que disponga de
  <a href="servicio-urgencias.html"><strong>atención de urgencias 24 horas</strong></a> no
  es un lujo: es una red de seguridad real. Ante una emergencia, lo primero es mantener la
  calma para poder evaluar el estado del animal. Evita moverlo bruscamente si sospechas una
  lesión musculoesquelética, controla posibles hemorragias con presión directa y llama a la
  clínica antes de salir para que el equipo pueda prepararse. Tener guardado el número de
  urgencias de tu veterinaria habitual —o de un centro de emergencias de referencia— es tan
  importante como tener el teléfono del médico de cabecera.
</p>
<p>
  Y si la duda es si algo que tu mascota ha comido puede hacerle daño, nuestra herramienta
  gratuita <a href="consultor-toxicos.html">«¿Puede comer esto?»</a> te orienta al momento
  sobre alimentos y plantas peligrosas. Orienta, no sustituye a una llamada: ante la duda,
  telefonea siempre.
</p>

<h2 id="preventiva">Medicina preventiva y salud animal</h2>
<p>
  La medicina preventiva es la inversión más rentable que puede hacer un propietario de
  mascota. Un animal que recibe chequeos periódicos, que sigue su calendario vacunal y que
  está correctamente desparasitado tiene muchas más probabilidades de vivir más años y con
  mejor calidad de vida.
</p>
<p>
  El <strong>chequeo anual</strong> permite detectar de forma temprana alteraciones en
  órganos vitales, cambios de peso significativos o el inicio de enfermedades silenciosas
  como la insuficiencia renal crónica. El <strong>calendario de vacunas</strong> varía
  según la especie, la edad y el estilo de vida del animal, por lo que el veterinario debe
  adaptarlo a cada caso: puedes hacerte una idea con nuestro
  <a href="calendario-mascota.html">calendario orientativo de la mascota</a>. La
  <strong>desparasitación interna y externa</strong> —frente a pulgas, garrapatas, gusano
  del corazón o parásitos intestinales— protege al animal y reduce el riesgo de zoonosis,
  es decir, de enfermedades transmisibles a las personas.
</p>
<p>
  A la prevención pertenece también la
  <a href="servicio-identificacion.html">identificación por microchip</a>, obligatoria para
  perros en la Comunidad de Madrid, y el control del peso, que puedes estimar con nuestra
  <a href="calculadora-nutricion.html">calculadora de ración</a>.
</p>

<h2 id="tecnologia">Tecnología y diagnóstico veterinario avanzado</h2>
<p>
  El diagnóstico preciso es la base de cualquier tratamiento eficaz, y la tecnología
  disponible en las clínicas veterinarias modernas ha avanzado considerablemente en la
  última década.
</p>
<p>
  La <strong>ecografía</strong> permite explorar órganos abdominales en tiempo real sin
  necesidad de sedación, lo que reduce el estrés del animal. La <strong>radiografía
  digital</strong> ofrece imágenes de alta resolución de manera inmediata, con una
  exposición a la radiación inferior a la de los sistemas analógicos tradicionales. Los
  <strong>analizadores de laboratorio internos</strong> hacen posible obtener resultados de
  hemogramas, bioquímicas y urianálisis en minutos, agilizando la toma de decisiones en
  situaciones urgentes y en la <a href="servicio-hospitalizacion.html">hospitalización</a>.
</p>
<p>
  Algunas clínicas madrileñas de referencia incorporan también
  <strong>electrocardiografía</strong>, <strong>endoscopia</strong> y acceso a
  <strong>resonancia magnética</strong> mediante derivación, lo que amplía notablemente el
  abanico diagnóstico sin necesidad de trasladar al animal a centros externos.
</p>

<h2 id="conclusion">En resumen</h2>
<p>
  Encontrar tu veterinaria de confianza en Madrid es un proceso que merece tiempo y
  atención. No se trata solo de buscar el centro más cercano o el más económico, sino de
  elegir un equipo que combine rigor clínico, tecnología adecuada, disponibilidad en
  urgencias y, sobre todo, un trato humano hacia el animal y hacia quien lo cuida. Una buena
  veterinaria acompaña a tu mascota durante toda su vida: desde las primeras vacunas hasta
  los controles de la edad adulta. Esa relación, construida con confianza y continuidad, es
  la mejor garantía de salud que puedes ofrecerle.
</p>
""",
    faqs=[
        ("¿Cuánto cuesta una consulta veterinaria en Madrid?",
         "El precio de una consulta general oscila habitualmente entre 30 y 60 euros, aunque "
         "varía según el tipo de clínica y la especialidad. Las urgencias nocturnas o festivas "
         "suelen tener un recargo."),
        ("¿Existen seguros de salud para mascotas?",
         "Sí. Varias aseguradoras ofrecen pólizas que cubren consultas, cirugías y "
         "hospitalización. Conviene comparar coberturas, franquicias y exclusiones antes de "
         "contratar."),
        ("¿Qué debo llevar en la primera visita?",
         "Si el animal ya tiene historial veterinario, aporta la cartilla sanitaria o el "
         "documento de vacunación. Si es una primera consulta en un cachorro, el veterinario "
         "te orientará sobre los primeros pasos."),
        ("¿Es obligatorio el microchip en Madrid?",
         "En la Comunidad de Madrid, el microchip es obligatorio para perros. Su implantación "
         "suele realizarse en la propia clínica y el coste es reducido. También es el requisito "
         "previo para inscribir al animal en el censo municipal."),
        ("¿Puedo cambiar de veterinario sin perder el historial de mi mascota?",
         "Sí. Tienes derecho a solicitar el historial clínico de tu mascota y trasladarlo a "
         "cualquier otro centro."),
    ],
    cta=("¿Buscas veterinaria en Madrid?",
         "Consulta general, medicina preventiva y urgencias 24 h en un mismo equipo. "
         "Llámanos o pide cita cuando te venga bien."),
)

GUIAS = [GUIA_VETERINARIA]
