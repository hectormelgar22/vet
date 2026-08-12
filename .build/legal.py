# -*- coding: utf-8 -*-
"""Textos legales. Ver nota de honestidad al final del archivo."""

TODO = '<span class="todo">COMPLETAR</span>'

DRAFT = """      <div class="draft-note">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
          <path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <p>
          <strong>Texto de partida, pendiente de revisión.</strong>
          Está redactado sobre la LSSI-CE, el RGPD, la LOPDGDD y las guías de la AEPD,
          pero los datos marcados como <span class="todo">COMPLETAR</span> solo los puede
          aportar la clínica, y conviene que un profesional lo revise antes de publicarlo.
          Nada de lo que hay aquí es asesoramiento jurídico.
        </p>
      </div>
"""

AVISO = dict(
    slug="aviso-legal",
    title="Aviso legal",
    meta="Aviso legal e información del titular del sitio web de Clínica Veterinaria Vitalis.",
    lede="Quién está detrás de esta web, en qué condiciones puedes usarla y qué puedes esperar de la información que publicamos.",
    toc=[
        ("titular", "Titular del sitio"),
        ("objeto", "Objeto"),
        ("uso", "Condiciones de uso"),
        ("propiedad", "Propiedad intelectual"),
        ("responsabilidad", "Responsabilidad"),
        ("enlaces", "Enlaces a terceros"),
        ("sanitaria", "Sobre la información veterinaria"),
        ("ley", "Ley aplicable"),
    ],
    body=f"""
<h2 id="titular">1. Titular del sitio</h2>
<p>
  En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la
  información y de comercio electrónico (LSSI-CE), se informa de los datos del titular:
</p>
<dl>
  <dt>Denominación social</dt>
  <dd>{TODO} (razón social completa)</dd>
  <dt>Nombre comercial</dt>
  <dd>Clínica Veterinaria Vitalis</dd>
  <dt>NIF / CIF</dt>
  <dd>{TODO}</dd>
  <dt>Domicilio</dt>
  <dd>Calle de Alcalá, 415 · 28027 Madrid</dd>
  <dt>Teléfono</dt>
  <dd><a href="tel:+34910305305">910 305 305</a></dd>
  <dt>Correo electrónico</dt>
  <dd><a href="mailto:citas@vitalisveterinaria.es">citas@vitalisveterinaria.es</a></dd>
  <dt>Datos registrales</dt>
  <dd>{TODO} (Registro Mercantil: tomo, folio, hoja e inscripción, si aplica)</dd>
  <dt>Autorización sanitaria</dt>
  <dd>
    Centro veterinario inscrito en el Registro de Centros Veterinarios de la Comunidad de
    Madrid con el número RCV-2871.
  </dd>
  <dt>Dirección técnica</dt>
  <dd>
    Elena Marín, colegiada nº 28345 del Ilustre Colegio Oficial de Veterinarios de Madrid.
  </dd>
  <dt>Proveedor de alojamiento</dt>
  <dd>{TODO} (nombre, domicilio y país del servidor)</dd>
</dl>

<h2 id="objeto">2. Objeto</h2>
<p>
  Este sitio web tiene una finalidad informativa: dar a conocer los servicios veterinarios
  de la clínica, sus instalaciones, su equipo y sus datos de contacto, y permitir solicitar
  cita. No es una tienda en línea ni permite contratar servicios de pago a distancia.
</p>

<h2 id="uso">3. Condiciones de uso</h2>
<p>
  El acceso a la web es gratuito y no requiere registro, salvo para los formularios de
  contacto. Al usarla te comprometes a hacerlo conforme a la ley y a la buena fe, y a no:
</p>
<ul>
  <li>Introducir datos falsos, de terceros sin su permiso o contenidos ilícitos.</li>
  <li>Intentar acceder a áreas restringidas, alterar el sitio o interferir en su funcionamiento.</li>
  <li>Usar medios automatizados que degraden el servicio para el resto de usuarios.</li>
</ul>
<p>
  Nos reservamos el derecho de retirar el acceso a quien incumpla estas condiciones, así
  como de modificar en cualquier momento la presentación, los contenidos y los servicios.
</p>

<h2 id="propiedad">4. Propiedad intelectual e industrial</h2>
<p>
  Los textos, el diseño, la estructura de navegación, las marcas y los logotipos de este
  sitio pertenecen al titular o cuenta con licencia para su uso. Queda prohibida su
  reproducción, distribución o transformación sin autorización expresa, salvo los usos
  permitidos por la ley (por ejemplo, la cita).
</p>
<p>
  Las fotografías e imágenes de mascotas e instalaciones que ilustran la web proceden de
  bancos de imágenes con licencia de uso comercial, o son propiedad de la clínica. Si
  detectas un contenido que consideras que vulnera derechos de terceros, escríbenos a
  <a href="mailto:citas@vitalisveterinaria.es">citas@vitalisveterinaria.es</a> y lo
  revisaremos de inmediato.
</p>

<h2 id="responsabilidad">5. Responsabilidad</h2>
<p>
  Ponemos cuidado en que la información esté actualizada y sea correcta, pero no podemos
  garantizar que esté libre de errores ni que el servicio se preste sin interrupciones.
  No respondemos de los daños derivados de:
</p>
<ul>
  <li>Fallos o desconexiones de las redes de telecomunicaciones ajenas a nuestro control.</li>
  <li>Un uso de la web contrario a estas condiciones.</li>
  <li>La presencia de software malicioso introducido por terceros.</li>
</ul>

<h2 id="enlaces">6. Enlaces a terceros</h2>
<p>
  Si la web incluye enlaces a sitios de terceros, lo hace únicamente para facilitar el
  acceso a información que puede resultarte útil. No controlamos esos sitios ni asumimos
  responsabilidad sobre sus contenidos ni sobre el tratamiento que hagan de tus datos.
</p>

<h2 id="sanitaria">7. Sobre la información veterinaria publicada</h2>
<p>
  <strong>Los contenidos de esta web tienen carácter divulgativo y no sustituyen a una
  consulta veterinaria.</strong> Esto incluye expresamente la herramienta de orientación
  «¿Qué le pasa?» de la página de inicio: ofrece una guía general según la especie y el
  motivo indicado, pero no es un diagnóstico y no puede valorar a un animal concreto.
</p>
<p>
  Solo una exploración presencial permite valorar a tu animal. Ante cualquier duda, o si
  observas signos de urgencia, llama al <a href="tel:+34910305305">910 305 305</a>.
</p>

<h2 id="ley">8. Ley aplicable y jurisdicción</h2>
<p>
  Estas condiciones se rigen por la legislación española. Para cualquier controversia,
  las partes se someten a los juzgados y tribunales del domicilio del usuario cuando este
  tenga la condición de consumidor; en el resto de casos, a los de {TODO} (ciudad).
</p>
""")

PRIVACIDAD = dict(
    slug="privacidad",
    title="Política de privacidad",
    meta="Cómo trata Clínica Veterinaria Vitalis los datos personales de tutores y pacientes: finalidades, base jurídica, plazos y derechos.",
    lede="Qué datos recogemos, para qué los usamos, cuánto los guardamos y cómo puedes controlarlos en cualquier momento.",
    toc=[
        ("responsable", "Responsable"),
        ("datos", "Datos que tratamos"),
        ("finalidades", "Finalidades y base jurídica"),
        ("plazos", "Cuánto los conservamos"),
        ("destinatarios", "Quién accede a ellos"),
        ("secreto", "Secreto profesional"),
        ("derechos", "Tus derechos"),
        ("seguridad", "Seguridad"),
        ("menores", "Menores"),
        ("cambios", "Cambios"),
    ],
    body=f"""
<h2 id="responsable">1. Responsable del tratamiento</h2>
<dl>
  <dt>Responsable</dt>
  <dd>{TODO} (razón social) — NIF {TODO}</dd>
  <dt>Domicilio</dt>
  <dd>Calle de Alcalá, 415 · 28027 Madrid</dd>
  <dt>Contacto para privacidad</dt>
  <dd><a href="mailto:citas@vitalisveterinaria.es">citas@vitalisveterinaria.es</a></dd>
  <dt>Delegado de Protección de Datos</dt>
  <dd>{TODO} (si se ha designado; no siempre es obligatorio)</dd>
</dl>

<h2 id="datos">2. Qué datos tratamos</h2>
<h3>Si nos escribes por el formulario de la web</h3>
<ul>
  <li>Nombre y apellidos.</li>
  <li>Teléfono y, si lo facilitas, correo electrónico.</li>
  <li>El motivo de consulta que redactes y los datos del animal que incluyas.</li>
  <li>La marca temporal del envío y tu decisión sobre los consentimientos.</li>
</ul>
<p>
  El formulario incluye un campo oculto anti-spam que ningún usuario ve ni rellena; solo
  sirve para descartar envíos automáticos.
</p>

<h3>Si tu animal es paciente de la clínica</h3>
<ul>
  <li>Datos identificativos y de contacto del tutor, necesarios para la facturación y el seguimiento.</li>
  <li>Historia clínica del animal: exploraciones, pruebas, diagnósticos, tratamientos y evolución.</li>
  <li>Número de microchip y datos de identificación registral.</li>
</ul>
<p>
  <strong>La historia clínica es del animal, no un dato de salud tuyo</strong>, pero se
  vincula a tus datos personales como tutor, y por eso queda amparada por esta política.
</p>

<h2 id="finalidades">3. Para qué los usamos y con qué base jurídica</h2>
<dl>
  <dt>Atender tu solicitud de cita o tu consulta</dt>
  <dd>Base: tu consentimiento al enviar el formulario (art. 6.1.a RGPD) y la aplicación de medidas precontractuales a tu petición (art. 6.1.b).</dd>
  <dt>Prestar el servicio veterinario y llevar la historia clínica</dt>
  <dd>Base: la ejecución del contrato de servicios (art. 6.1.b) y el cumplimiento de obligaciones legales de registro sanitario (art. 6.1.c).</dd>
  <dt>Facturación y obligaciones fiscales y contables</dt>
  <dd>Base: obligación legal (art. 6.1.c).</dd>
  <dt>Recordatorios de vacunación, revisiones y desparasitación</dt>
  <dd>Base: interés legítimo en el seguimiento sanitario del paciente (art. 6.1.f), o tu consentimiento cuando el aviso tenga contenido comercial.</dd>
  <dt>Enviarte comunicaciones comerciales</dt>
  <dd>Base: tu consentimiento expreso, que es <strong>voluntario y separado</strong> (casilla independiente, nunca premarcada) y puedes retirar cuando quieras.</dd>
</dl>
<p>
  No tomamos decisiones automatizadas con efectos jurídicos sobre ti ni elaboramos perfiles
  con tus datos.
</p>

<h2 id="plazos">4. Cuánto tiempo los conservamos</h2>
<ul>
  <li><strong>Consultas que no derivan en visita:</strong> hasta un año desde el último contacto.</li>
  <li><strong>Historia clínica:</strong> mientras el animal sea paciente y, después, durante los plazos de prescripción de responsabilidades derivadas del servicio.</li>
  <li><strong>Facturación:</strong> los plazos fiscales y contables aplicables (con carácter general, entre cuatro y seis años).</li>
  <li><strong>Consentimiento comercial:</strong> hasta que lo retires.</li>
</ul>
<p>Cumplidos los plazos, los datos se bloquean y después se suprimen de forma segura.</p>

<h2 id="destinatarios">5. Quién accede a tus datos</h2>
<p>
  <strong>No vendemos ni cedemos tus datos a terceros con fines comerciales.</strong>
  Pueden acceder a ellos, en la medida imprescindible:
</p>
<ul>
  <li>El equipo clínico y administrativo de la clínica.</li>
  <li>Proveedores que actúan como encargados del tratamiento (alojamiento web, software de gestión clínica, laboratorio externo, asesoría), con contrato de encargo firmado conforme al art. 28 RGPD.</li>
  <li>Centros de referencia a los que te derivemos, cuando el caso lo exija y con tu conocimiento.</li>
  <li>Administraciones públicas, cuando exista obligación legal (por ejemplo, el registro de identificación animal).</li>
</ul>
<p>
  No están previstas transferencias internacionales de datos. Si algún proveedor las
  implicara, se informará y se ampararán en las garantías del capítulo V del RGPD.
</p>

<h2 id="secreto">6. Secreto profesional</h2>
<p>
  Lo que nos cuentes sobre tu animal está amparado por el secreto profesional veterinario
  y solo lo consulta el equipo que atiende el caso. No lo usamos para publicidad ni lo
  compartimos fuera de los supuestos del apartado anterior.
</p>

<h2 id="derechos">7. Tus derechos</h2>
<p>Puedes ejercer en cualquier momento los derechos de:</p>
<ul>
  <li><strong>Acceso:</strong> saber qué datos tuyos tratamos.</li>
  <li><strong>Rectificación:</strong> corregir los que sean inexactos.</li>
  <li><strong>Supresión:</strong> pedir que los borremos cuando ya no sean necesarios.</li>
  <li><strong>Limitación:</strong> pedir que los conservemos sin usarlos mientras se resuelve una reclamación.</li>
  <li><strong>Oposición:</strong> oponerte a los tratamientos basados en interés legítimo.</li>
  <li><strong>Portabilidad:</strong> recibir tus datos en un formato estructurado y de uso común.</li>
  <li><strong>Retirar el consentimiento</strong> en cualquier momento, sin que afecte a la licitud del tratamiento anterior.</li>
</ul>
<p>
  Escríbenos a <a href="mailto:citas@vitalisveterinaria.es">citas@vitalisveterinaria.es</a>
  o acude a la clínica, indicando qué derecho quieres ejercer y acreditando tu identidad.
  Responderemos en el plazo máximo de un mes.
</p>
<p>
  Si consideras que no hemos atendido bien tu solicitud, puedes reclamar ante la
  <strong>Agencia Española de Protección de Datos</strong> (C/ Jorge Juan 6, 28001 Madrid ·
  <a href="https://www.aepd.es" target="_blank" rel="noopener noreferrer">www.aepd.es</a>).
</p>

<h2 id="seguridad">8. Seguridad</h2>
<p>
  Aplicamos medidas técnicas y organizativas apropiadas al riesgo: control de acceso por
  usuario al software clínico, copias de seguridad, cifrado del sitio web mediante HTTPS y
  formación del equipo en confidencialidad. Ningún sistema es infalible, pero revisamos
  periódicamente estas medidas.
</p>

<h2 id="menores">9. Menores de edad</h2>
<p>
  Los formularios de esta web están dirigidos a mayores de 14 años. Si eres menor de esa
  edad, pide a tu madre, padre o tutor que contacte con nosotros.
</p>

<h2 id="cambios">10. Cambios en esta política</h2>
<p>
  Si cambian los tratamientos o la normativa, actualizaremos este texto y modificaremos la
  fecha de la última revisión que figura al principio. Te recomendamos consultarlo de vez
  en cuando.
</p>
""")

COOKIES = dict(
    slug="cookies",
    title="Política de cookies",
    meta="Qué cookies y almacenamiento local usa la web de Clínica Veterinaria Vitalis, y cómo cambiar tu decisión en cualquier momento.",
    lede="Esta web funciona sin cookies de seguimiento salvo que tú las aceptes. Aquí tienes exactamente qué se guarda y cómo cambiarlo.",
    toc=[
        ("que-son", "Qué son"),
        ("que-usamos", "Qué usamos ahora"),
        ("consentimiento", "Cómo pedimos consentimiento"),
        ("cambiar", "Cambiar tu decisión"),
        ("navegador", "Borrarlas del navegador"),
        ("terceros", "Terceros"),
    ],
    body=f"""
<h2 id="que-son">1. Qué son las cookies</h2>
<p>
  Una cookie es un pequeño archivo que un sitio web guarda en tu dispositivo al visitarlo.
  Sirven para recordar información entre páginas o entre visitas. Junto a ellas existen
  tecnologías equivalentes, como el <em>almacenamiento local</em> del navegador, sujetas a
  las mismas reglas de consentimiento.
</p>

<h2 id="que-usamos">2. Qué usamos ahora mismo</h2>
<p>
  Esta web es deliberadamente austera: <strong>no incrusta mapas, vídeos de terceros,
  botones sociales ni píxeles publicitarios</strong>, que son la vía habitual por la que se
  cuelan cookies sin que el usuario lo sepa. En este momento solo se guarda un dato:
</p>

<div class="table-wrap">
  <table class="data-table">
    <caption class="sr-only">Cookies y almacenamiento local utilizados</caption>
    <thead>
      <tr>
        <th scope="col">Nombre</th>
        <th scope="col">Tipo</th>
        <th scope="col">Finalidad</th>
        <th scope="col">Duración</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>vc_consent_v2</code></td>
        <td>Técnica propia<br>(almacenamiento local)</td>
        <td>Recordar si has aceptado o rechazado las cookies de medición, para no volver a preguntártelo en cada visita.</td>
        <td>180 días</td>
      </tr>
    </tbody>
  </table>
</div>

<p>
  Al ser una cookie técnica necesaria para respetar tu propia decisión, está exenta del
  deber de consentimiento previo. Si la borras, volveremos a mostrarte el aviso.
</p>

<h3>Si en el futuro se activa la analítica</h3>
<p>
  La web está preparada para incorporar una herramienta de medición ({TODO}: indicar cuál,
  por ejemplo Google Analytics 4). <strong>Hasta que no se configure y tú la aceptes, no se
  descarga ni escribe nada.</strong> Cuando se active, este apartado se ampliará con el
  nombre de cada cookie, su titular, su finalidad y su duración.
</p>

<h2 id="consentimiento">3. Cómo pedimos tu consentimiento</h2>
<ul>
  <li>Al entrar por primera vez verás un aviso con dos botones, <strong>«Rechazar todo» y «Aceptar todo», con la misma prominencia</strong>, como pide la guía de la AEPD. Rechazar cuesta lo mismo que aceptar: un clic.</li>
  <li>Mientras no decidas, todo el almacenamiento de medición y publicidad permanece <strong>denegado por defecto</strong> (Consent Mode v2), no solo «sin usar».</li>
  <li>Cerrar el aviso con la tecla <kbd>Esc</kbd> equivale a rechazar. El silencio nunca se interpreta como aceptación.</li>
  <li>Tu decisión se renueva a los 180 días, muy por debajo del máximo de 24 meses que recomienda la AEPD.</li>
</ul>

<h2 id="cambiar">4. Cambiar tu decisión</h2>
<p>
  Puedes revisarla cuando quieras desde el enlace <strong>«Preferencias de cookies»</strong>
  del pie de página, presente en todas las páginas de este sitio, o desde aquí mismo:
</p>
<p>
  <button class="btn btn--outline js-open-cookies" type="button">Abrir preferencias de cookies</button>
</p>

<h2 id="navegador">5. Borrarlas desde el navegador</h2>
<p>
  También puedes gestionarlas o eliminarlas directamente en tu navegador. Ten en cuenta que
  si borras el almacenamiento de este sitio, se olvidará tu decisión y volveremos a
  preguntarte:
</p>
<ul>
  <li><a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener noreferrer">Google Chrome</a></li>
  <li><a href="https://support.mozilla.org/es/kb/Borrar%20cookies" target="_blank" rel="noopener noreferrer">Mozilla Firefox</a></li>
  <li><a href="https://support.apple.com/es-es/guide/safari/sfri11471/mac" target="_blank" rel="noopener noreferrer">Safari</a></li>
  <li><a href="https://support.microsoft.com/es-es/microsoft-edge" target="_blank" rel="noopener noreferrer">Microsoft Edge</a></li>
</ul>

<h2 id="terceros">6. Cookies de terceros</h2>
<p>
  Las tipografías se sirven desde Google Fonts y las bibliotecas de animación desde una red
  de distribución de contenidos (jsDelivr). Estos servicios <strong>no instalan cookies</strong>,
  pero sí reciben tu dirección IP como parte de la petición, algo inevitable en cualquier
  recurso servido desde otro dominio. Si prefieres evitarlo por completo, ambos recursos
  pueden alojarse en el propio servidor; está anotado como mejora pendiente.
</p>
<p>
  El mapa de la página de contacto <strong>no está incrustado</strong> precisamente para no
  cargar cookies de Google antes de que decidas.
</p>
""")

LEGALES = [AVISO, PRIVACIDAD, COOKIES]

# ---------------------------------------------------------------------------
# NOTA DE HONESTIDAD
# Estos textos NO son asesoramiento jurídico ni un documento listo para
# publicar. Están construidos sobre la estructura que exigen la LSSI-CE, el
# RGPD, la LOPDGDD y las guías de la AEPD, y describen con exactitud lo que la
# web hace hoy (comprobado en el código: solo `vc_consent_v2` en localStorage,
# Consent Mode denegado por defecto, sin mapa incrustado). Pero los datos
# identificativos y registrales de una empresa real no se pueden inventar: van
# marcados como COMPLETAR y son visibles a propósito, para que nadie publique
# la página por descuido creyéndola terminada.
# ---------------------------------------------------------------------------
