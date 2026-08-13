# -*- coding: utf-8 -*-
"""Artículos / guías informativas (contenido SEO).

Cada guía es un dict con la misma forma que los servicios/legales, para que
`build.py` la ensamble con la misma cabecera, pie y banner de cookies. El texto
es divulgativo (orientado al dueño de la mascota), no clínico: no da pautas ni
dosis, así que no necesita firma colegiada como las herramientas. Enlaza a las
páginas de servicio y a las herramientas para reforzar el enlazado interno.

El cuerpo está redactado en el tono cercano del resto del sitio (segunda
persona, frases de longitud variable) y evita los tics de redacción de IA:
sin guiones largos, sin negrita mecánica, sin cierres grandilocuentes. Las
palabras clave, los títulos y los enlaces internos se mantienen intactos para
no perder posicionamiento.
"""

# NOTA CLIENTE: verificar la cifra del censo antes de publicarla como dato con
# fuente. El Ayuntamiento de Madrid publica el censo de animales de compañía;
# la cifra exacta cambia cada año. Si no se puede citar con seguridad, cambiar
# "más de 300.000 perros" por "cientos de miles de perros".

GUIA_VETERINARIA = dict(
    slug="guia-veterinaria-madrid",
    title="Veterinaria de confianza en Madrid: guía para elegir bien | Clínica Veterinaria Vitalis",
    meta=("Guía para elegir veterinaria en Madrid: servicios esenciales, urgencias 24 h, "
          "medicina preventiva, diagnóstico avanzado y preguntas frecuentes sobre el cuidado animal."),
    h1="Tu veterinaria de confianza en Madrid para el cuidado animal",
    lede=("Qué distingue a una buena clínica veterinaria, qué debería ofrecerte y cómo "
          "reaccionar el día que tu mascota te necesite de verdad."),
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
  Madrid es una ciudad de animales. En la capital hay más de 300.000 perros registrados en
  el censo municipal, y cada año se suman más gatos, conejos y otras mascotas. Con tantos
  animales en casa, elegir una veterinaria de confianza no es un trámite: es una de las
  decisiones que más pesan cuando cuidas de uno. Esta guía te ayuda a entender qué
  distingue a una buena clínica veterinaria, qué debería ofrecerte y cómo reaccionar el
  día que tu mascota te necesite de verdad.
</p>

<h2 id="que-es">¿Qué es una veterinaria de confianza?</h2>
<p>
  Una clínica veterinaria de confianza no se mide solo por su equipamiento o por lo cerca
  que la tengas. Se mide, sobre todo, por la relación que construye con el animal y con su
  familia a lo largo del tiempo. Un buen centro tiene profesionales colegiados con
  experiencia, te explica los diagnósticos y los tratamientos sin tecnicismos, y trata
  igual de bien a un golden retriever de doce años que a un hámster que acabas de llevar a
  casa.
</p>
<p>
  Hay otras señales que ayudan a fiarte: presupuestos claros por escrito, disposición a
  resolver dudas fuera de la consulta y la honestidad de derivarte a un especialista cuando
  el caso lo pide. En Madrid, con la oferta que hay, todo esto pesa cada vez más, y no solo
  tener la clínica a la vuelta de la esquina.
</p>

<h2 id="servicios">Servicios veterinarios esenciales en Madrid</h2>
<p>
  Una clínica completa debería cubrir, como mínimo, lo que un animal necesita en cada etapa
  de su vida.
</p>
<p>
  Las <a href="servicio-consulta.html">consultas de medicina general</a> son la puerta de
  entrada: la revisión anual, el diagnóstico de lo más común y el seguimiento de
  enfermedades crónicas como la diabetes o la artritis. Junto a ellas van los programas de
  <a href="servicio-preventiva.html">vacunación</a>, que protegen tanto al animal como a
  las personas de su alrededor frente al moquillo, la rabia o la leucemia felina.
</p>
<p>
  La <a href="servicio-cirugia.html">cirugía veterinaria</a> va desde una esterilización o
  una limpieza dental hasta intervenciones bastante más complejas, y para todas hacen falta
  un quirófano en condiciones y alguien que controle la
  <a href="servicio-anestesia.html">anestesia</a> de cerca. Y luego está el
  <a href="servicio-urgencias.html">servicio de urgencias</a>, que es el que de verdad se
  nota cuando algo va mal: una intoxicación, un atropello o una dificultad para respirar no
  esperan a que abra la clínica.
</p>

<h2 id="elegir">Cómo elegir la mejor veterinaria en Madrid</h2>
<p>
  Con cientos de clínicas repartidas por los distritos de la capital, la elección abruma.
  Merece la pena fijarse en cuatro cosas.
</p>
<p>
  La cercanía importa más de lo que parece: en una urgencia, llegar en diez minutos puede
  cambiarlo todo. Un horario amplio, con sábados por la mañana incluidos, evita que una
  revisión de rutina se convierta en un lío de agenda.
</p>
<p>
  Las especialidades disponibles ganan peso según el animal envejece o aparecen problemas
  concretos: dermatología, oftalmología, oncología o traumatología no están en todas
  partes. Y las opiniones de otros dueños, ya sea en Google, en foros o en el grupo del
  barrio, te cuentan lo que ninguna clínica dice de sí misma: cómo tratan, cuánto se espera
  y si de verdad te explican las cosas.
</p>

<h2 id="urgencias">Atención veterinaria de urgencias en Madrid</h2>
<p>
  A ningún dueño le gusta pensarlo, pero una emergencia le puede tocar a cualquiera. Una
  pelea con otro perro, un bocado a algo tóxico o una caída pueden pasar en cualquier
  momento, también a las tres de la madrugada de un domingo festivo.
</p>
<p>
  Por eso tranquiliza tanto tener cerca una veterinaria con
  <a href="servicio-urgencias.html">atención de urgencias 24 horas</a>. Si te toca vivir
  una, lo primero es no perder la calma para poder valorar cómo está el animal. No lo
  muevas de golpe si sospechas que se ha hecho daño en huesos o articulaciones, corta
  cualquier hemorragia con presión directa y llama a la clínica antes de salir, para que te
  esperen preparados. Tener a mano el número de urgencias de tu veterinaria vale tanto como
  tener el del médico de cabecera.
</p>
<p>
  Y si la duda es si eso que se ha comido le puede hacer daño, nuestra herramienta gratuita
  <a href="consultor-toxicos.html">«¿Puede comer esto?»</a> te da una primera orientación
  sobre alimentos y plantas peligrosas. Orienta, no sustituye a la llamada: ante la duda,
  telefonea siempre.
</p>

<h2 id="preventiva">Medicina preventiva y salud animal</h2>
<p>
  Si algo sale a cuenta de verdad, es la medicina preventiva. Un animal con las revisiones
  al día, el calendario de vacunas en regla y bien desparasitado vive más años y con mejor
  salud.
</p>
<p>
  En la revisión anual se pillan a tiempo cosas que por fuera no se ven: un riñón que
  empieza a fallar, un cambio de peso que se ha ido de las manos, una enfermedad silenciosa
  como la insuficiencia renal. El calendario de vacunas no es igual para todos; depende de
  la especie, la edad y la vida que lleve el animal, así que lo ajusta el veterinario. Para
  hacerte una idea, puedes usar nuestro
  <a href="calendario-mascota.html">calendario orientativo de la mascota</a>. La
  desparasitación, por dentro y por fuera, lo protege de pulgas, garrapatas, gusano del
  corazón o lombrices, y de paso reduce el riesgo de zoonosis, esas enfermedades que
  también pueden pasar a las personas.
</p>
<p>
  A la prevención pertenece también la
  <a href="servicio-identificacion.html">identificación por microchip</a>, obligatoria para
  perros en la Comunidad de Madrid, y vigilar el peso, que puedes estimar con nuestra
  <a href="calculadora-nutricion.html">calculadora de ración</a>.
</p>

<h2 id="tecnologia">Tecnología y diagnóstico veterinario avanzado</h2>
<p>
  Un buen diagnóstico es la base de cualquier tratamiento, y en la última década la
  tecnología de las clínicas ha dado un salto grande.
</p>
<p>
  La ecografía deja ver los órganos del abdomen en tiempo real y casi siempre sin sedar,
  con lo que el animal pasa menos estrés. La radiografía digital da imágenes nítidas al
  momento y con menos radiación que la placa de toda la vida. Y con un laboratorio propio
  se sacan hemogramas, bioquímicas o análisis de orina en minutos, que es justo lo que hace
  falta en una urgencia o durante la
  <a href="servicio-hospitalizacion.html">hospitalización</a>.
</p>
<p>
  Las clínicas mejor equipadas de Madrid añaden electrocardiografía, endoscopia o, por
  derivación, resonancia magnética, y así resuelven mucho sin tener que mandar al animal a
  otro centro.
</p>

<h2 id="conclusion">En resumen</h2>
<p>
  Elegir veterinaria en Madrid lleva su tiempo, y merece la pena dárselo. No va de quedarte
  con la más barata ni con la más cercana, sino con un equipo que junte buen criterio
  clínico, medios suficientes, urgencias cuando hagan falta y trato de verdad, tanto para
  el animal como para ti. Una buena clínica te acompaña durante toda la vida de tu mascota,
  desde la primera vacuna hasta las revisiones de mayor. Esa continuidad, más que ninguna
  otra cosa, es lo que cuida su salud.
</p>
""",
    faqs=[
        ("¿Cuánto cuesta una consulta veterinaria en Madrid?",
         "Una consulta general suele costar entre 30 y 60 euros, según la clínica y la "
         "especialidad. Las urgencias de noche o en festivo llevan un recargo aparte."),
        ("¿Existen seguros de salud para mascotas?",
         "Sí. Varias aseguradoras ofrecen pólizas que cubren consultas, cirugías y "
         "hospitalización. Antes de contratar, compara bien las coberturas, las franquicias "
         "y lo que queda excluido."),
        ("¿Qué debo llevar en la primera visita?",
         "Si tu mascota ya tiene historial, lleva la cartilla sanitaria o el documento de "
         "vacunación. Si es un cachorro que estrena veterinario, no necesitas nada: allí te "
         "orientan sobre los primeros pasos."),
        ("¿Es obligatorio el microchip en Madrid?",
         "En la Comunidad de Madrid, el microchip es obligatorio para los perros. Se implanta "
         "en la propia clínica, cuesta poco y es el paso previo para inscribir al animal en "
         "el censo municipal."),
        ("¿Puedo cambiar de veterinario sin perder el historial de mi mascota?",
         "Sí. Tienes derecho a pedir el historial clínico de tu mascota y llevarlo a "
         "cualquier otro centro."),
    ],
    cta=("¿Buscas veterinaria en Madrid?",
         "Consulta general, medicina preventiva y urgencias 24 h en un mismo equipo. "
         "Llámanos o pide cita cuando te venga bien."),
)

GUIAS = [GUIA_VETERINARIA]
