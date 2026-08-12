# -*- coding: utf-8 -*-
"""Contenido de las páginas de detalle de cada servicio.

Los textos son divulgativos y prudentes: describen cómo se trabaja, no
prometen resultados ni sustituyen una consulta. Los datos que dependen de la
clínica real (precios concretos, marcas de equipos) se dejan fuera a propósito.
"""

SERVICIOS = [
dict(
  slug="servicio-urgencias",
  nav="Urgencias 24 h",
  name="Urgencias 24 h",
  h1="Urgencias 24 h, <em>365 días</em>",
  title="Urgencias veterinarias 24 h en Madrid | Clínica Veterinaria Vitalis",
  meta="Urgencias veterinarias 24 horas en Madrid, con veterinario y auxiliar presentes en la clínica. Llama antes de salir: preparamos sala, vía y medicación.",
  lede="Guardia presencial de verdad: un veterinario y un auxiliar dentro de la clínica a cualquier hora, no un teléfono que avisa a alguien que está en su casa.",
  img="assets/img/servicios/urgencias",
  alt="Dos veterinarios colocan una vía a un perro durante una urgencia.",
  badges=["Presencial 24 h", "Sin cita previa", "Estabilización inmediata"],
  facts=[("24 h", "de guardia presencial, todos los días del año"),
         ("0 min", "de espera para un animal inestable: entra directo"),
         ("1 llamada", "y preparamos todo mientras llegas")],
  steps=[
    ("Llama antes de salir de casa",
     "Es el minuto mejor invertido. Con lo que nos cuentes preparamos la sala, la vía, el oxígeno y la medicación que previsiblemente vamos a necesitar. También te decimos cómo moverlo para no empeorar una lesión."),
    ("Triaje al llegar",
     "Al entrar valoramos primero lo que mata: vía aérea, respiración, circulación y nivel de consciencia. Un animal inestable pasa por delante de cualquier consulta programada, y te lo explicamos si te toca esperar."),
    ("Estabilizar antes que diagnosticar",
     "Primero se corrige lo que compromete la vida —oxígeno, fluidos, analgesia, control de hemorragias— y solo después se buscan pruebas. Diagnosticar a un paciente que se está descompensando es perder tiempo."),
    ("Te contamos qué pasa y qué cuesta",
     "En cuanto está estable te explicamos qué hemos encontrado, qué proponemos y cuánto va a costar. Si hay que ingresar, te damos un presupuesto antes de seguir, salvo que la demora suponga un riesgo."),
  ],
  body="""
<h2>Qué consideramos una urgencia</h2>
<p>
  Si dudas, llama: valorar por teléfono es gratis y preferimos mil consultas de más a una
  de menos. Dicho eso, estos signos son motivo de salir hacia la clínica sin esperar:
</p>
<ul>
  <li><strong>Dificultad para respirar</strong>, respiración con la boca abierta en gatos, o encías azuladas o muy pálidas.</li>
  <li><strong>Abdomen hinchado y duro</strong>, sobre todo si intenta vomitar sin sacar nada: puede ser una torsión gástrica.</li>
  <li><strong>Convulsiones</strong>, o más de una crisis seguida.</li>
  <li><strong>Sangrado que no para</strong> tras cinco minutos de presión.</li>
  <li><strong>Golpe fuerte o atropello</strong>, aunque camine y parezca estar bien.</li>
  <li><strong>Un macho que intenta orinar y no lo consigue</strong>: la obstrucción urinaria es una emergencia vital.</li>
  <li><strong>Parto detenido</strong> con contracciones sin expulsión durante más de media hora.</li>
  <li><strong>Sospecha de intoxicación.</strong> Trae el envase si lo tienes.</li>
</ul>

<h2>Qué NO hacer mientras vienes</h2>
<ul>
  <li><strong>No des analgésicos humanos.</strong> El ibuprofeno y el paracetamol son tóxicos para perros y gatos; el paracetamol puede matar a un gato con una sola dosis.</li>
  <li><strong>No provoques el vómito por tu cuenta</strong> en una intoxicación: con cáusticos o derivados del petróleo empeora el daño.</li>
  <li><strong>No le des de comer ni de beber</strong> si sospechas que va a necesitar anestesia.</li>
  <li><strong>No aprietes el transportín</strong> a un gato que respira mal: llévalo abierto y en ambiente fresco.</li>
</ul>
""",
  note=("Sobre el coste de una urgencia",
        ["La atención de urgencia tiene un precio superior al de una consulta programada, porque implica personal disponible en horario nocturno y festivo. Te lo decimos antes de empezar, no al final.",
         "Si el presupuesto es un problema, dilo cuanto antes. Hay decisiones clínicas que se pueden escalonar y opciones intermedias que podemos plantear, pero solo si lo hablamos a tiempo."]),
  faqs=[("¿Hay alguien físicamente en la clínica de madrugada?",
         "Sí. Un veterinario y un auxiliar, dentro del centro. No es un teléfono de aviso que localiza a alguien en su domicilio y tarda media hora en llegar."),
        ("¿Tengo que pedir cita para una urgencia?",
         "No. Ven directamente. Lo único que te pedimos es que llames por el camino para que podamos preparar la sala y ganar minutos."),
        ("¿Atendéis animales que no son pacientes vuestros?",
         "Sí, sin ningún problema. Si tu animal se trata habitualmente en otra clínica, le pasamos el informe completo de lo que hemos hecho para que su veterinario siga el caso.")],
  related=["servicio-anestesia", "servicio-cirugia", "servicio-hospitalizacion"],
  cta=("¿Tu animal está mal ahora mismo?",
       "No esperes a mañana para ver si mejora. Llama y lo valoramos por teléfono contigo; si hay que venir, te lo decimos.")
),

dict(
  slug="servicio-consulta",
  nav="Consulta y medicina interna",
  name="Consulta y medicina interna",
  h1="Consulta y <em>medicina interna</em>",
  title="Consulta veterinaria y medicina interna en Madrid | Clínica Veterinaria Vitalis",
  meta="Consulta veterinaria sin prisas en Madrid: exploración completa, analítica propia, ecografía y radiología para llegar a un diagnóstico que se sostenga.",
  lede="Exploración completa sin reloj en la mano. Si algo no encaja, lo investigamos hasta tener una explicación que se sostenga.",
  img="assets/img/servicios/consulta",
  alt="Veterinario explora a un perro sobre la mesa de consulta.",
  badges=["30 min por visita", "Analítica en el día", "Ecografía y radiología"],
  facts=[("30 min", "de consulta, para poder explorar y explicar"),
         ("60 min", "para la analítica básica, sin enviarla fuera"),
         ("1 responsable", "del caso, de principio a fin")],
  steps=[
    ("Escuchar la historia",
     "Buena parte del diagnóstico está en lo que cuentas: desde cuándo, con qué frecuencia, si come igual, si bebe más, si ha cambiado algo en casa. Suele decir más que cualquier prueba, y por eso no lo despachamos en dos minutos."),
    ("Explorar entero, no solo lo que duele",
     "Peso, temperatura, mucosas, auscultación cardiaca y pulmonar, palpación abdominal, ganglios, boca, piel y oídos. Muchos hallazgos importantes aparecen lejos del motivo de la visita."),
    ("Proponer pruebas con una hipótesis detrás",
     "No pedimos una batería completa «por si acaso». Cada prueba responde a una pregunta concreta y te explicamos cuál es antes de hacerla, con su coste."),
    ("Un plan que se pueda cumplir en casa",
     "Un tratamiento perfecto que no se puede administrar no sirve. Ajustamos formatos y pautas a tu animal y a tu día a día, y te lo damos por escrito."),
  ],
  body="""
<h2>Qué podemos resolver aquí mismo</h2>
<p>Tenemos en la clínica los medios para cerrar la mayoría de los casos sin derivar:</p>
<ul>
  <li><strong>Analítica propia:</strong> hemograma y bioquímica en aproximadamente una hora, lo que permite decidir en la misma visita.</li>
  <li><strong>Ecografía abdominal</strong> para valorar hígado, bazo, riñones, vejiga, intestino y útero.</li>
  <li><strong>Radiología digital</strong> de tórax, abdomen y sistema locomotor.</li>
  <li><strong>Citologías</strong> de piel, oído y masas superficiales, con lectura en el momento.</li>
  <li><strong>Control de tensión arterial</strong>, especialmente relevante en gatos mayores.</li>
</ul>

<h2>Procesos crónicos: el seguimiento importa más que el diagnóstico</h2>
<p>
  Enfermedades como la insuficiencia renal, la diabetes, el hipertiroidismo felino, la
  cardiopatía o la artrosis no se resuelven en una visita: se controlan durante años. En
  estos casos trabajamos con un calendario de revisiones acordado contigo, ajustes de dosis
  según los controles y un objetivo realista, que muchas veces no es curar sino que el
  animal viva bien el mayor tiempo posible.
</p>

<h2>Cuándo te diremos que acudas a otro sitio</h2>
<p>
  Hay casos que exigen medios o experiencia que no tenemos: oncología compleja, neurocirugía,
  resonancia magnética, cirugía torácica avanzada. Cuando toca, lo decimos claramente y te
  derivamos a un centro de referencia con el informe y las pruebas ya hechas, para que no
  tengas que empezar de cero ni pagar dos veces lo mismo.
</p>
""",
  note=("Lo que no vas a oír aquí",
        ["No te vamos a proponer pruebas cuyo resultado no vaya a cambiar nada de lo que hagamos después. Si una analítica no va a modificar el tratamiento, te lo diremos en vez de facturarla.",
         "Y si no sabemos qué tiene, te lo diremos también. Es más útil que un diagnóstico inventado para cerrar la visita."]),
  faqs=[("¿Cuánto dura una consulta?",
         "Reservamos unos 30 minutos. Si el caso es complejo y necesita más, preferimos citarte de nuevo con tiempo antes que atenderte con prisas."),
        ("¿Puedo llevar pruebas hechas en otra clínica?",
         "Sí, y nos ayuda mucho. Tráelas en papel o en digital: evitan repetir pruebas, ahorran dinero y permiten ver la evolución."),
        ("¿Atendéis animales exóticos?",
         "Atendemos perros y gatos. Con conejos, roedores, aves y reptiles, llámanos antes: te confirmamos si podemos ayudarte o a qué centro de referencia acudir.")],
  related=["servicio-preventiva", "servicio-anestesia", "servicio-urgencias"],
  cta=("¿Le notas algo raro y no sabes si es para hoy?",
       "Cuéntanoslo por teléfono. Muchas veces se resuelve con una cita tranquila esta semana, y saberlo te quita la preocupación.")
),

dict(
  slug="servicio-preventiva",
  nav="Vacunación y preventiva",
  name="Vacunación y medicina preventiva",
  h1="Vacunación y <em>medicina preventiva</em>",
  title="Vacunación y medicina preventiva veterinaria en Madrid | Clínica Veterinaria Vitalis",
  meta="Calendario de vacunación adaptado a la edad, la raza y la vida real de tu mascota, con desparasitación y revisiones. Te avisamos nosotros cuando toca.",
  lede="Calendario adaptado a la edad, la raza y la vida real de tu animal. Te avisamos nosotros cuando toca; no tienes que acordarte.",
  img="assets/img/servicios/vacunacion",
  alt="Veterinaria administra una vacuna a un perro pequeño.",
  badges=["Calendario personalizado", "Avisos automáticos", "Revisión incluida"],
  facts=[("2 min", "dura el pinchazo; el resto es la revisión"),
         ("1 vez al año", "como mínimo, aunque esté perfectamente"),
         ("0 olvidos", "te avisamos nosotros por teléfono o correo")],
  steps=[
    ("Revisión antes de vacunar",
     "Nunca vacunamos sin explorar. Un animal con fiebre, inmunodeprimido o incubando algo no debe recibir una vacuna ese día: la respuesta sería peor y podríamos enmascarar un problema."),
    ("Un calendario para este animal, no uno genérico",
     "No es lo mismo un gato que no sale de casa que uno con acceso al exterior, ni un perro de ciudad que uno que va al campo o viaja. Vacunamos contra lo que tu animal puede encontrarse de verdad."),
    ("Desparasitación ajustada al riesgo",
     "Interna y externa, con la frecuencia que corresponda a su vida y a la época del año. En Madrid el control de flebotomos, vector de la leishmaniosis, merece atención especial en los meses cálidos."),
    ("Nosotros llevamos la cuenta",
     "Al salir queda registrada la próxima fecha y te avisamos cuando se acerca. Es nuestro trabajo recordarlo, no el tuyo."),
  ],
  body="""
<h2>Qué incluye una visita preventiva</h2>
<ul>
  <li>Exploración general completa y control de peso.</li>
  <li>Revisión de la boca, que es donde antes se detecta la enfermedad periodontal.</li>
  <li>Actualización de vacunas según el calendario acordado.</li>
  <li>Desparasitación interna y externa.</li>
  <li>Revisión del microchip y de que sus datos registrales siguen siendo correctos.</li>
  <li>Consejo sobre alimentación y peso, que es la intervención preventiva más rentable que existe.</li>
</ul>

<h2>Etapas de la vida, necesidades distintas</h2>
<h3>Cachorros y gatitos</h3>
<p>
  La primovacunación se hace por fases durante las primeras semanas, porque los anticuerpos
  que reciben de la madre interfieren con la vacuna hasta cierta edad. Es también el momento
  de hablar de socialización, alimentación y del microchip.
</p>
<h3>Adultos</h3>
<p>
  Una revisión anual con actualización de vacunas. En animales sanos suele ser una visita
  corta, y sirve sobre todo para detectar a tiempo cambios de peso, soplos, bultos o
  problemas dentales.
</p>
<h3>Mayores</h3>
<p>
  A partir de los siete años (antes en razas grandes) recomendamos <strong>dos revisiones al
  año y una analítica anual</strong>. La enfermedad renal, el hipertiroidismo felino o la
  artrosis dan la cara tarde, y detectarlos pronto cambia mucho el pronóstico.
</p>

<h2>Peso: el factor que más años suma</h2>
<p>
  El sobrepeso acorta la vida y agrava casi todo lo demás: articulaciones, corazón, diabetes,
  riesgo anestésico. Si tu animal está por encima de su peso ideal te lo diremos, con una
  pauta concreta y controles de seguimiento. No es una regañina: es probablemente lo más
  eficaz que podemos hacer por él.
</p>
""",
  note=None,
  faqs=[("Mi gato no sale de casa, ¿necesita vacunas?",
         "Sí, aunque menos. Algunos virus entran en casa en la ropa o el calzado, y la situación cambia si en algún momento se escapa, viaja o convive con otro gato. Ajustamos el calendario a su caso real."),
        ("¿Qué pasa si se me ha pasado la fecha de refuerzo?",
         "Llámanos. Según cuánto tiempo haya pasado y de qué vacuna se trate, a veces basta con una dosis y otras hay que reiniciar la pauta. No lo dejes por vergüenza: es muy habitual."),
        ("¿Puede tener reacción a la vacuna?",
         "Es poco frecuente. Lo normal es algo de decaimiento o molestia en el punto del pinchazo durante 24 o 48 horas. Si aparece hinchazón facial, vómitos o dificultad respiratoria, llámanos de inmediato.")],
  related=["servicio-identificacion", "servicio-consulta", "servicio-hospitalizacion"],
  cta=("¿No sabes si le toca algo este año?",
       "Dinos su nombre y lo miramos en su ficha. Si le toca, lo dejamos citado en la misma llamada.")
),

dict(
  slug="servicio-identificacion",
  nav="Microchip y pasaporte",
  name="Microchip, pasaporte e identificación",
  h1="Microchip, pasaporte e <em>identificación</em>",
  title="Microchip y pasaporte europeo para mascotas en Madrid | Clínica Veterinaria Vitalis",
  meta="Implantación de microchip, alta en el registro de la Comunidad de Madrid y pasaporte europeo en la misma visita, con la documentación lista para viajar.",
  lede="Implantación, alta en el registro autonómico y pasaporte europeo en la misma visita, con la documentación lista para viajar.",
  img="assets/img/servicios/identificacion",
  alt="Veterinario implanta un microchip a un perro que sujeta su tutor.",
  badges=["Alta en el registro oficial", "Pasaporte europeo", "En una sola visita"],
  facts=[("1 visita", "para chip, alta registral y pasaporte"),
         ("Obligatorio", "en perros, gatos y hurones en la Comunidad de Madrid"),
         ("21 días", "de antelación mínima si vais a viajar por la UE")],
  steps=[
    ("Implantación",
     "El microchip se coloca bajo la piel del lado izquierdo del cuello con una aguja algo más gruesa que la de una vacuna. Se hace en segundos y no requiere anestesia; la mayoría de los animales apenas se inmutan."),
    ("Lectura y comprobación",
     "Leemos el chip inmediatamente para verificar que responde y que el número coincide con el de la etiqueta. También leemos siempre a los animales que llegan por primera vez, por si ya llevan uno antiguo."),
    ("Alta en el registro oficial",
     "Damos de alta el número junto a tus datos de contacto en el registro de identificación de animales de compañía de la Comunidad de Madrid. Un chip sin registrar, o registrado con un teléfono antiguo, no sirve para nada."),
    ("Pasaporte, si lo necesitas",
     "Emitimos el pasaporte europeo, que recoge la identificación, la vacuna antirrábica y los tratamientos aplicados. Es el documento que te van a pedir en la frontera."),
  ],
  body="""
<h2>Por qué el registro importa más que el chip</h2>
<p>
  El microchip no lleva GPS ni datos dentro: es solo un número. Ese número únicamente sirve
  si está asociado a un teléfono al que alguien conteste. La causa más frecuente de que un
  animal encontrado no vuelva a casa <strong>no es que no lleve chip, sino que los datos del
  registro están desactualizados</strong>.
</p>
<p>Avísanos siempre que cambies de teléfono, de domicilio o de titularidad del animal. Es gratis y se hace en un minuto.</p>

<h2>Viajar por la Unión Europea</h2>
<p>Para moverte con tu animal dentro de la UE necesitas tres cosas, y en este orden:</p>
<ol>
  <li><strong>Microchip</strong> implantado y registrado.</li>
  <li><strong>Vacuna antirrábica</strong> válida, puesta <em>después</em> del microchip. Si se pone antes, no cuenta.</li>
  <li><strong>Pasaporte europeo</strong> emitido por un veterinario autorizado.</li>
</ol>
<p>
  La vacuna antirrábica no es válida hasta <strong>21 días después</strong> de administrarla
  en una primovacunación. Es el error que más viajes estropea: planifica con margen.
</p>
<p>
  Algunos destinos añaden requisitos propios —tratamiento frente a <em>Echinococcus</em>
  para entrar en Irlanda, Malta, Finlandia o Noruega, por ejemplo— y los países fuera de la
  UE tienen sus propias reglas, a veces con análisis serológicos y meses de antelación.
  Dinos a dónde vas y lo comprobamos contigo.
</p>

<h2>Perros potencialmente peligrosos</h2>
<p>
  Si tu perro está dentro de esta categoría, además de la identificación necesitas licencia
  municipal y seguro de responsabilidad civil. Podemos emitirte el certificado veterinario
  de aptitud que suele exigir el ayuntamiento como parte del trámite.
</p>
""",
  note=("Un recordatorio incómodo pero útil",
        ["Abandonar un animal es delito, y también lo es no identificarlo cuando la norma lo exige. Pero el motivo de fondo para tener el chip al día es más simple: es lo único que hace que alguien pueda devolvértelo si un día se pierde."]),
  faqs=[("¿Duele?",
         "Es un pinchazo con una aguja algo más gruesa de lo habitual. Molesta un momento y ya está. Muchas veces lo aprovechamos para hacerlo en la misma visita de la vacuna o durante una castración, ya bajo anestesia."),
        ("¿Se puede poner a cualquier edad?",
         "Sí, desde las pocas semanas de vida. En la Comunidad de Madrid debe estar puesto y registrado dentro de los plazos que fija la normativa; si tienes dudas con las fechas, llámanos."),
        ("He adoptado un animal que ya tiene chip, ¿qué hago?",
         "Hay que cambiar la titularidad en el registro. Trae la documentación de la adopción o el contrato de compraventa y lo tramitamos nosotros.")],
  related=["servicio-preventiva", "servicio-consulta", "servicio-urgencias"],
  cta=("¿Vas a viajar con tu animal?",
       "Cuéntanos el destino y la fecha y comprobamos qué necesita y con cuánta antelación. Mejor sobrado de tiempo que a la carrera.")
),

dict(
  slug="servicio-anestesia",
  nav="Anestesia y dolor",
  name="Anestesia monitorizada y manejo del dolor",
  h1="Anestesia monitorizada y <em>manejo del dolor</em>",
  title="Anestesia veterinaria monitorizada y control del dolor | Clínica Veterinaria Vitalis",
  meta="Protocolo anestésico individual, analítica preanestésica y constantes vigiladas minuto a minuto. El dolor se trata antes de que aparezca.",
  lede="Protocolo individual por paciente y constantes vigiladas minuto a minuto. El dolor se trata antes de que aparezca, no cuando ya está.",
  img="assets/img/servicios/anestesia",
  alt="Veterinaria realiza una ecografía de control a un perro.",
  badges=["Analítica previa siempre", "Monitorización continua", "Analgesia preventiva"],
  facts=[("100 %", "de los pacientes con analítica preanestésica"),
         ("5 constantes", "vigiladas de forma continua durante el procedimiento"),
         ("1 persona", "dedicada solo a la anestesia, además del cirujano")],
  steps=[
    ("Valoración previa",
     "Exploración, historia clínica y analítica preanestésica para conocer la función hepática y renal, que son las que van a metabolizar y eliminar los fármacos. En pacientes mayores o cardiópatas añadimos las pruebas que hagan falta."),
    ("Un protocolo para este paciente",
     "La combinación de fármacos y las dosis se calculan según especie, raza, edad, peso, estado y tipo de intervención. Un galgo, un bulldog y un gato mayor no reciben lo mismo, porque no responden igual."),
    ("Vigilancia continua, por una persona dedicada",
     "Durante todo el procedimiento se controlan frecuencia y ritmo cardiaco, saturación de oxígeno, capnografía, tensión arterial y temperatura. De eso se encarga alguien cuya única tarea es esa; el cirujano opera."),
    ("Despertar acompañado",
     "El despertar es un momento delicado. El paciente permanece en zona de recuperación con manta térmica y vigilancia hasta que recupera reflejos, temperatura y postura con normalidad."),
  ],
  body="""
<h2>El dolor se previene, no se persigue</h2>
<p>
  Un principio básico de la anestesiología moderna: es mucho más eficaz administrar
  analgesia <em>antes</em> del estímulo doloroso que intentar controlarlo cuando ya está
  instaurado. Por eso la analgesia empieza en la premedicación y continúa durante y después
  de la intervención, combinando fármacos con mecanismos distintos para usar dosis menores
  de cada uno.
</p>
<p>
  Cuando el procedimiento lo permite añadimos <strong>anestesia locorregional</strong>
  —bloqueos nerviosos, epidural—, que reduce la cantidad de anestesia general necesaria y
  mejora mucho el despertar.
</p>

<h2>Cómo reconocer el dolor en casa</h2>
<p>
  Perros y gatos no se quejan como nosotros; tienden a esconder el dolor. Estas señales sí
  lo indican:
</p>
<ul>
  <li>Postura encogida, tensión abdominal o reticencia a tumbarse.</li>
  <li>Dejar de comer, de saltar o de subir escaleras.</li>
  <li>Lamerse de forma insistente una zona concreta.</li>
  <li>Cambios de carácter: esconderse, gruñir al tocarlo, buscar aislamiento.</li>
  <li>Respiración rápida y superficial en reposo.</li>
</ul>
<p>Si ves algo de esto tras un procedimiento, llámanos: la pauta se puede ajustar.</p>

<h2>Sobre el riesgo anestésico</h2>
<p>
  Toda anestesia tiene riesgo, y quien te diga lo contrario no está siendo honesto. En
  animales sanos y con una monitorización adecuada ese riesgo es bajo, y aumenta con la
  edad, la obesidad, las cardiopatías y las razas braquicéfalas. Nuestro trabajo es
  conocerlo antes, reducirlo con lo que está en nuestra mano y explicártelo con claridad
  para que decidas con la información delante.
</p>
""",
  note=("El ayuno, bien hecho",
        ["Te daremos las pautas por escrito. Con carácter general, la comida se retira unas horas antes, pero el agua se suele mantener hasta poco antes de la cita: un ayuno de agua prolongado deshidrata y complica la anestesia.",
         "En cachorros, animales muy pequeños y diabéticos las pautas cambian. No improvises: síguelas tal como te las demos y, si te has despistado, dínoslo al llegar en vez de callarlo."]),
  faqs=[("¿Es necesaria la analítica previa aunque parezca sano?",
         "Sí, y la hacemos siempre. Buena parte de las alteraciones hepáticas o renales relevantes no dan ningún síntoma visible, y son precisamente las que cambian el protocolo anestésico."),
        ("Mi perro es braquicéfalo (bulldog, carlino...), ¿hay más riesgo?",
         "Sí, su anatomía complica la vía aérea y el despertar. Lo tenemos en cuenta en el protocolo, en la monitorización y en la vigilancia posterior, que suele ser más prolongada."),
        ("¿Puedo quedarme con él hasta que se duerma?",
         "Puedes acompañarle hasta la zona de preanestesia. A partir de ahí se trabaja en un área limpia con acceso restringido, por seguridad del paciente.")],
  related=["servicio-cirugia", "servicio-hospitalizacion", "servicio-consulta"],
  cta=("¿Te preocupa que lo tengan que dormir?",
       "Es una preocupación razonable. Llámanos y te explicamos exactamente qué se le va a hacer y cómo lo vigilamos.")
),

dict(
  slug="servicio-cirugia",
  nav="Cirugía y traumatología",
  name="Cirugía de tejidos blandos y traumatología",
  h1="Cirugía y <em>traumatología</em>",
  title="Cirugía veterinaria y traumatología en Madrid | Clínica Veterinaria Vitalis",
  meta="Quirófano propio, instrumental esterilizado con control de cada ciclo y un cirujano responsable del caso de principio a fin. Presupuesto cerrado por escrito.",
  lede="Quirófano propio, instrumental esterilizado con control de cada ciclo y un cirujano responsable del caso de principio a fin.",
  img="assets/img/servicios/cirugia",
  alt="Equipo quirúrgico durante una intervención.",
  badges=["Quirófano propio", "Presupuesto cerrado", "Un cirujano por caso"],
  facts=[("1 quirófano", "de uso exclusivo, independiente de la consulta"),
         ("Cada ciclo", "de autoclave con control y registro"),
         ("0 sorpresas", "el presupuesto se cierra por escrito antes de entrar")],
  steps=[
    ("Valoración y planificación",
     "Exploración, pruebas de imagen y analítica preanestésica. La cirugía se planifica entera antes de la primera incisión: abordaje, material, tiempos previstos y también la vuelta a casa."),
    ("Presupuesto por escrito",
     "Antes de entrar a quirófano te damos el presupuesto cerrado, con lo que incluye y lo que no. Si durante la intervención apareciera algo que lo modifique, se te llama antes de continuar."),
    ("Quirófano y esterilidad",
     "Zona quirúrgica independiente, con circuito limpio y material esterilizado en autoclave. Cada ciclo se controla y se registra: no basta con que el aparato se haya puesto en marcha."),
    ("Alta con instrucciones claras",
     "Te vas con la pauta de analgesia, el cuidado de la herida, qué está permitido y qué no, señales de alarma y la fecha de revisión. Por escrito, porque nadie retiene eso en una conversación de cinco minutos."),
  ],
  body="""
<h2>Qué operamos</h2>
<h3>Tejidos blandos</h3>
<ul>
  <li>Esterilización y castración de perros y gatos.</li>
  <li>Extirpación de masas cutáneas y subcutáneas, con envío a laboratorio para su análisis.</li>
  <li>Cirugía digestiva: cuerpos extraños, gastropexia, resección intestinal.</li>
  <li>Cirugía de urgencia: torsión gástrica, piometra, cesárea, hernias.</li>
  <li>Cirugía urinaria: desobstrucción y cistotomía.</li>
</ul>
<h3>Traumatología</h3>
<ul>
  <li>Fracturas: osteosíntesis con placas, agujas o fijadores externos según el caso.</li>
  <li>Luxación de rótula.</li>
  <li>Rotura de ligamento cruzado.</li>
  <li>Heridas complejas y reconstrucción.</li>
</ul>

<h2>Sobre las masas: no esperar es la clave</h2>
<p>
  Un bulto que crece, cambia de aspecto o sangra debe verse pronto. Muchas veces la punción
  con aguja fina permite orientar el diagnóstico en la propia consulta. Y cuando hay que
  extirpar, <strong>una masa pequeña se opera con márgenes cómodos y cierre sencillo</strong>;
  la misma masa seis meses después puede requerir una cirugía mucho mayor. La biopsia se
  envía siempre a laboratorio, aunque «tenga buena pinta».
</p>

<h2>La recuperación en casa es parte de la cirugía</h2>
<p>
  El resultado depende tanto del quirófano como de las dos semanas siguientes. Lo que más
  se estropea en casa:
</p>
<ul>
  <li><strong>El collar o el body.</strong> Un solo lametón puede abrir una herida que iba perfecta. Se mantiene hasta la retirada de puntos, también de noche.</li>
  <li><strong>El reposo.</strong> «Se encuentra bien» no significa que el hueso o el tejido hayan cicatrizado. Las restricciones de ejercicio se cumplen enteras.</li>
  <li><strong>La analgesia completa.</strong> No la retires porque parezca que ya no le duele: precisamente por eso está funcionando.</li>
</ul>
""",
  note=("Cuándo llamarnos tras una cirugía",
        ["Herida enrojecida, caliente, hinchada o con secreción; puntos abiertos; sangrado; decaimiento marcado; fiebre; vómitos repetidos; o que deje de comer más de un día.",
         "No esperes a la revisión programada si ves algo de esto. Llamar de más no molesta a nadie."]),
  faqs=[("¿Cuándo puedo esterilizar a mi mascota?",
         "Depende de la especie, la raza y el tamaño; en razas grandes suele convenir esperar más. Es una decisión que se toma caso por caso, valorando ventajas e inconvenientes contigo."),
        ("¿El presupuesto puede cambiar durante la operación?",
         "Solo si aparece un hallazgo imprevisto, y en ese caso te llamamos antes de continuar, salvo que detenerse suponga un riesgo vital. Nunca te encontrarás una factura mayor sin haberlo hablado."),
        ("¿Se queda ingresado después de operarse?",
         "Depende del procedimiento. Muchas cirugías programadas se van a casa el mismo día, ya despiertas y con la analgesia puesta. Otras requieren ingreso, y te lo decimos de antemano.")],
  related=["servicio-anestesia", "servicio-hospitalizacion", "servicio-urgencias"],
  cta=("¿Le han dicho que hay que operar y tienes dudas?",
       "Una segunda opinión no ofende a nadie. Trae las pruebas que tengas y lo valoramos contigo sin compromiso.")
),

dict(
  slug="servicio-hospitalizacion",
  nav="Hospitalización 24 h",
  name="Hospitalización con vigilancia 24 h",
  h1="Hospitalización con <em>vigilancia 24 h</em>",
  title="Hospitalización veterinaria 24 h en Madrid | Clínica Veterinaria Vitalis",
  meta="Boxes separados para perros y gatos, control de constantes por turnos, registro de cada dosis y parte diario para el tutor a la misma hora.",
  lede="Boxes separados para perros y gatos, control de constantes por turnos y parte diario para ti, sin tener que perseguirnos.",
  img="assets/img/servicios/hospitalizacion",
  alt="Perro descansando abrigado durante su recuperación.",
  badges=["Vigilancia presencial", "Zona felina separada", "Parte diario"],
  facts=[("24 h", "con personal dentro del centro, también de madrugada"),
         ("1 parte al día", "a la misma hora, con lo bueno y lo malo"),
         ("2 zonas", "separadas: perros y gatos no comparten espacio")],
  steps=[
    ("Ingreso y plan escrito",
     "Al ingresar se fija el plan: fluidoterapia, medicación con horarios, controles previstos y objetivos concretos para las próximas horas. Queda escrito para que todos los turnos trabajen igual."),
    ("Controles por turnos",
     "Constantes, estado general, dolor, apetito, orina y heces. Cada dosis administrada se registra con hora y firma, de modo que en cualquier momento se sabe qué ha recibido y cuándo."),
    ("Una llamada al día, a la misma hora",
     "Te llamamos nosotros, a una hora acordada, con la evolución real: lo que va bien y lo que no. Y si algo cambia de forma relevante, no esperamos a la llamada del día siguiente."),
    ("Alta con el caso cerrado",
     "Te vas con el informe completo, la medicación explicada, la pauta escrita y la revisión programada. Si tu veterinario habitual es otro, le mandamos el informe."),
  ],
  body="""
<h2>Por qué perros y gatos no comparten espacio</h2>
<p>
  Un gato hospitalizado que oye y huele perros a un metro está en estrés permanente, y el
  estrés retrasa la recuperación de forma medible: come menos, se mueve menos y responde
  peor al tratamiento. Por eso la zona felina está separada, con menos ruido, escondites
  dentro del box y manipulación mínima.
</p>

<h2>Visitas</h2>
<p>
  En ingresos de varios días, ver a su familia suele ayudar. Organizamos visitas en horario
  acordado siempre que el estado del paciente lo permita. En algunos casos —animales muy
  inestables, o que se alteran mucho al despedirse— puede ser contraproducente, y entonces
  te lo diremos con franqueza y buscaremos alternativas, como enviarte fotos o vídeos.
</p>

<h2>Lo que puedes traer</h2>
<ul>
  <li>Su manta o una prenda con tu olor: ayuda más de lo que parece, sobre todo en gatos.</li>
  <li>Su comida habitual, si sigue una dieta concreta o es muy selectivo.</li>
  <li>La medicación que ya esté tomando, en su envase original.</li>
</ul>
<p>Los juguetes que puedan desmontarse o tragarse, mejor en casa.</p>

<h2>Hablar de pronóstico sin rodeos</h2>
<p>
  Cuando un ingreso se complica, te lo diremos claramente y con tiempo, incluyendo cuando la
  mejor opción para el animal ya no sea seguir tratando. Preferimos una conversación difícil
  a tiempo que una factura creciente sin un horizonte realista. Esa decisión es tuya, pero
  no vas a tomarla sin información ni sola.
</p>
""",
  note=None,
  faqs=[("¿Hay alguien de noche o se quedan solos?",
         "Hay personal dentro de la clínica las 24 horas. Un animal ingresado que se descompensa de madrugada es atendido en ese momento, no a la mañana siguiente."),
        ("¿Puedo llamar yo si estoy preocupado?",
         "Claro. Te llamamos una vez al día a la hora acordada, pero puedes llamar cuando lo necesites. Si estamos en mitad de una urgencia te lo diremos y te devolvemos la llamada."),
        ("¿Cómo se factura un ingreso?",
         "Se estima al ingresar y se te informa de la evolución del gasto durante la estancia. Si el importe se aproxima a lo previsto y el tratamiento va a continuar, te avisamos antes de seguir sumando.")],
  related=["servicio-urgencias", "servicio-cirugia", "servicio-anestesia"],
  cta=("¿Tienes dudas sobre un ingreso?",
       "Llámanos y te explicamos cómo trabajamos, qué vigilamos y cómo te vamos a informar cada día.")
),
]
