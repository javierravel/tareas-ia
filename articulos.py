GUIA = "https://javiautomates.gumroad.com/l/guia-gratis"
CURSO_N8N = "https://www.youtube.com/watch?v=lAOP_nrNvY4"
CANAL = "https://www.youtube.com/@javiautomates"

# Generado el 26/11/2026 desde el sitio publicado (13 artículos) + 5 nuevos. "video": None = sin video incrustado.
ARTICULOS = [
{
"slug": "informe-a-diapositivas-con-ia",
"num": 1,
"titulo": "Cómo convertir un informe en diapositivas con IA (en 5 minutos)",
"corto": "Informe → diapositivas",
"desc": "Subí tu informe a Claude con este prompt y obtené 8 diapositivas con título, 3 puntos, sugerencia de imagen y notas del orador. Prompt listo para copiar.",
"video": "hBXKjzYjOWA",
"fecha": "2026-11-26",
"cuerpo": """
<p>Tenés el informe escrito, doce páginas, y te piden la presentación para el jueves. Pasar todo a diapositivas a mano lleva una tarde. Con IA lleva cinco minutos, y lo que te queda es revisar, no escribir.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>8 diapositivas, cada una con un título corto y 3 puntos.</li>
<li>Una sugerencia de imagen o gráfico para cada diapositiva.</li>
<li>Las notas del orador: lo que vas a decir, separado de lo que se ve en pantalla.</li>
<li>Una última diapositiva de "Próximos pasos".</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Abrí <a href="https://claude.ai" rel="nofollow">Claude</a> (sirve el plan gratis) y adjuntá el informe con el clip: Word, PDF o texto pegado.</li>
<li>Pegá el prompt de abajo y cambiá lo que está entre corchetes.</li>
<li>Leé la estructura que te propone. Si una diapositiva sobra o falta, pedíselo con una frase: "uní la 3 y la 4" o "agregá una de costos".</li>
<li>Pasá el resultado a PowerPoint, Google Slides o Keynote. Si usás Claude con creación de archivos activada, podés pedirle directamente el archivo .pptx.</li>
</ol>

{prompt}

<h2>El truco: pocas palabras en la pantalla</h2>
<p>El error más común en una presentación es copiar el informe en las diapositivas. Nadie lee un párrafo proyectado. Por eso el prompt limita el título a 6 palabras y pide 3 puntos cortos: todo lo demás va a las <strong>notas del orador</strong>, que vos ves y el público no.</p>

<h2>Antes de presentar, revisá esto</h2>
<ul>
<li><strong>Los números.</strong> Compará cada cifra con el informe original. La IA resume bien, pero un número mal copiado en una reunión cuesta caro.</li>
<li><strong>El público.</strong> No es lo mismo presentar a la dirección que al equipo. Cambiá [PÚBLICO] y el tono cambia solo.</li>
<li><strong>Datos sensibles.</strong> Si el informe tiene información confidencial de tu empresa, fijate qué permite tu organización antes de subirlo a cualquier IA.</li>
</ul>
""",
"prompt": "Convertí este documento en una presentación de 8 diapositivas para [PÚBLICO]. Cada diapositiva: un título de máximo 6 palabras, 3 puntos cortos y una sugerencia de imagen o gráfico. La última: \"Próximos pasos\". Agregá notas del orador.",
"faq": [
("¿Sirve con ChatGPT o Gemini?", "Sí, el prompt funciona igual en cualquier asistente que acepte documentos. Yo lo uso con Claude porque respeta bien los límites de largo."),
("¿Puede hacer el archivo de PowerPoint directamente?", "Claude puede crear archivos .pptx si tenés activada la creación de archivos. Si no, copiá el texto a tu plantilla: lleva dos minutos."),
],
},
{
"slug": "plantillas-whatsapp-con-ia",
"num": 2,
"titulo": "6 plantillas de WhatsApp para tu negocio, hechas con IA en 2 minutos",
"corto": "Plantillas de WhatsApp",
"desc": "Bienvenida, confirmación de turno, recordatorio de pago, pago vencido, pedido de reseña y fuera de horario: el prompt para que la IA te las escriba y cómo guardarlas como respuestas rápidas.",
"video": "IcNH3mEdEoI",
"fecha": "2026-11-26",
"cuerpo": """
<p>Recordatorio de pago, confirmación de turno, bienvenida a un cliente nuevo. Si tenés un negocio, escribís esos mensajes todos los días, y casi siempre a mano. Hacelos una vez bien y reusalos.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>6 plantillas cortas (máximo 50 palabras) adaptadas a tu rubro.</li>
<li>Espacios para completar como [NOMBRE] y [FECHA].</li>
<li>Todas guardadas como respuestas rápidas: escribís una barra y aparecen.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Abrí Claude y pegá el prompt de abajo. Cambiá [A QUÉ TE DEDICÁS] por tu rubro con detalle: "peluquería en Palermo, turnos por WhatsApp" funciona mejor que "peluquería".</li>
<li>Leé las 6 plantillas y pedile cambios de tono si hace falta: "más cálido", "tuteo en vez de usted", "sin emojis".</li>
<li>En <strong>WhatsApp Business</strong>, entrá a Herramientas para la empresa → Respuestas rápidas y creá una por plantilla, con un atajo fácil (por ejemplo <code>/turno</code>, <code>/pago</code>).</li>
<li>Cuando escribas a un cliente, tipeá <code>/</code> y elegí la que necesitás. Completás el nombre y la fecha, y listo.</li>
</ol>

{prompt}

<h2>Cuidado con el recordatorio de pago</h2>
<p>Es el mensaje más delicado: si suena a reclamo, perdés al cliente. El prompt pide uno "amable" y otro de "pago vencido" por separado. Usá primero el amable, y el de vencido solo si no hubo respuesta.</p>

<h2>Si no usás WhatsApp Business</h2>
<p>En el WhatsApp común no hay respuestas rápidas. Guardá las plantillas en una nota fijada del celular, o pasate a WhatsApp Business: es gratis y podés usar el mismo número.</p>
""",
"prompt": "Mi negocio es [A QUÉ TE DEDICÁS]. Escribime plantillas cortas para WhatsApp de: bienvenida, confirmación de turno, recordatorio de pago amable, pago vencido, pedido de reseña y fuera de horario. Máximo 50 palabras, con [NOMBRE] y [FECHA].",
"faq": [
("¿Puedo pedirle más de 6?", "Sí. Agregá a la lista lo que te pidan seguido: presupuesto enviado, pedido listo para retirar, cambio de horario."),
("¿Se pueden mandar automáticamente?", "Las respuestas rápidas no se mandan solas: las elegís vos. Para envíos automáticos hace falta la API de WhatsApp Business, que es otro nivel."),
],
},
{
"slug": "manual-de-procedimientos-con-ia",
"num": 3,
"titulo": "Cómo escribir un manual de procedimientos con IA (aunque lo expliques desordenado)",
"corto": "Manual de la tarea que solo vos sabés",
"desc": "Contale a la IA cómo hacés una tarea, aunque sea desordenado, y te devuelve un manual con objetivo, pasos numerados, errores comunes y cómo saber que quedó bien.",
"video": "qNwSzF7oj5o",
"fecha": "2026-11-26",
"cuerpo": """
<p>En toda oficina hay una tarea que solo sabe hacer una persona. El día que esa persona falta o se va de vacaciones, la tarea se frena. Escribir el manual siempre queda para después, porque sentarse a redactar un procedimiento es aburrido. Con IA no tenés que redactar: alcanza con contarlo.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Un procedimiento para alguien que nunca hizo la tarea.</li>
<li>Objetivo, qué necesita antes de empezar y pasos numerados.</li>
<li>Los errores comunes y cómo saber que la tarea quedó bien.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Contá la tarea como se la contarías a un compañero nuevo. No importa el orden: podés grabar un audio, pasarlo a texto y pegarlo tal cual.</li>
<li>Pegá el prompt de abajo con tu explicación en lugar de [EXPLICACIÓN].</li>
<li>Respondé las preguntas que te haga. Esta es la clave: Claude detecta lo que falta (qué sistema usás, qué pasa si algo falla) y te lo pregunta antes de inventarlo.</li>
<li>Probalo: dale el manual a alguien que no sepa hacer la tarea y mirá dónde se traba. Ahí está lo que hay que agregar.</li>
</ol>

{prompt}

<h2>El truco es la última frase</h2>
<p>"Si falta información, haceme preguntas." Sin esa frase, la IA completa los huecos con suposiciones que suenan bien y no son tu procedimiento. Con esa frase, te pregunta. Funciona en cualquier prompt donde la IA tenga que documentar algo que solo vos sabés.</p>

<h2>Ideas de tareas para documentar</h2>
<ul>
<li>El cierre de mes o la carga de facturas.</li>
<li>Cómo dar de alta a un empleado o un cliente nuevo en los sistemas.</li>
<li>Qué hacer cuando falla la impresora, el proyector o el sistema de turnos.</li>
<li>El paso a paso de un trámite que hacés una vez por año y siempre te olvidás.</li>
</ul>
""",
"prompt": "Te explico cómo hago esta tarea: [EXPLICACIÓN]. Convertilo en un procedimiento paso a paso para alguien nuevo: objetivo, qué necesita antes de empezar, pasos numerados, errores comunes y cómo saber que quedó bien. Si falta información, haceme preguntas.",
"faq": [
("¿En qué formato lo guardo?", "Pedile a Claude el manual en formato de documento y guardalo donde tu equipo ya busca las cosas: una carpeta compartida, el Drive o la wiki de la empresa."),
("¿Y si la tarea tiene pantallas?", "Agregá capturas después de cada paso. Un procedimiento con imágenes se sigue el doble de rápido."),
],
},
{
"slug": "recordatorio-diario-telegram-n8n",
"num": 4,
"titulo": "Recordatorio diario en el celular con n8n y Telegram (gratis y sin programar)",
"corto": "Mensaje diario con n8n + Telegram",
"desc": "Armá un flujo de 3 nodos en n8n que todos los días a las 8 te manda por Telegram lo que no te podés olvidar. Paso a paso para principiantes, sin código.",
"video": "CAUNrU-WNZM",
"fecha": "2026-11-26",
"cuerpo": """
<p>Todos los días a las ocho, un mensaje en tu celular con lo que no te podés olvidar: tomar la pastilla, mandar el reporte, regar las plantas. Lo armás una vez con <strong>n8n</strong> y un bot de Telegram, y corre solo.</p>

<h2>Qué necesitás</h2>
<ul>
<li><strong>n8n</strong>: es gratis si lo instalás en tu computadora. También hay versión en la nube, que es paga después del período de prueba.</li>
<li><strong>Telegram</strong> en el celular.</li>
<li>10 minutos.</li>
</ul>

<h2>Paso 1: creá tu bot de Telegram</h2>
<ol>
<li>En Telegram buscá <strong>@BotFather</strong> (tiene tilde azul) y escribile <code>/newbot</code>.</li>
<li>Elegí un nombre y un usuario que termine en "bot". BotFather te da un <strong>token</strong>: es una contraseña, no la compartas.</li>
<li>Abrí tu bot nuevo y tocá <strong>Iniciar</strong>. Sin este paso no te puede escribir.</li>
<li>Buscá <strong>@userinfobot</strong>, escribile cualquier cosa y anotá tu <strong>Id</strong>: es tu Chat ID.</li>
</ol>

<h2>Paso 2: el flujo de 3 nodos</h2>
<ol>
<li><strong>Schedule Trigger</strong>: todos los días, a las 8:00.</li>
<li><strong>Telegram → Send a text message</strong>: en la credencial pegás el token; en Chat ID, tu número; en Text, tu recordatorio.</li>
<li>En Additional Fields, apagá <strong>Append n8n Attribution</strong> para que no aparezca la firma de n8n.</li>
</ol>
<p>Probalo con <strong>Execute workflow</strong>: el mensaje te llega en segundos. Después tocá <strong>Publish</strong>. Si no lo publicás, no corre solo: es el error más común.</p>

<h2>Errores comunes</h2>
<ul>
<li><strong>"chat not found" o "Forbidden"</strong>: no tocaste Iniciar en tu bot, o el Chat ID tiene un número de más o de menos.</li>
<li><strong>Se queda esperando y da error de conexión</strong>: algunas redes de oficina o de universidad bloquean Telegram. Probá desde otra red.</li>
<li><strong>No llega a la mañana siguiente</strong>: n8n tiene que estar prendido a esa hora. Si lo tenés en tu compu, la compu también.</li>
</ul>

<h2>Para ir más lejos</h2>
<p>Este flujo es el esqueleto de casi cualquier automatización: <strong>disparador, datos, acción</strong>. Agregá en el medio un nodo que busque datos (el clima, tus tareas del día, un precio) y el mensaje se arma solo. Lo explico completo en el <a href="https://www.youtube.com/watch?v=lAOP_nrNvY4">curso gratis de n8n desde cero</a>.</p>
""",
"prompt": "",
"faq": [
("¿n8n es gratis?", "La versión que se instala en tu computadora o en tu servidor es gratis. La versión en la nube tiene prueba gratis y después es paga."),
("¿Puedo usar WhatsApp en vez de Telegram?", "Se puede, pero WhatsApp pide una cuenta de empresa y aprobaciones. Telegram es gratis, se arma en un minuto y no pide nada."),
],
},
{
"slug": "formulario-que-llena-una-tabla-n8n",
"num": 5,
"titulo": "Formulario que llena una tabla solo, con aviso por Telegram (n8n, sin código)",
"corto": "Formulario que llena la planilla",
"desc": "Dejá de copiar pedidos a mano: con n8n armás un formulario que guarda cada respuesta en una tabla y te avisa por Telegram. Gratis y sin programar.",
"video": "57bTYyM3HlQ",
"fecha": "2026-11-26",
"cuerpo": """
<p>Cada pedido que te llega por mail o por mensaje lo copiás a mano en una planilla. Copiás el nombre, el producto, la fecha… y alguno se te pasa. Con <strong>n8n</strong> armás un formulario que guarda cada respuesta en una tabla y, además, te avisa cuando alguien lo completa.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Un formulario con link propio para mandarle a tus clientes.</li>
<li>Una tabla que se llena sola, una fila por respuesta.</li>
<li>Un aviso por Telegram cada vez que entra un pedido.</li>
</ul>

<h2>Paso 1: la tabla</h2>
<p>n8n trae sus propias tablas (<strong>Data tables</strong>), sin conectar Google ni otra cuenta. En la pantalla principal, entrá a Data tables → Create data table y creá las columnas que necesites: por ejemplo <code>fecha</code>, <code>nombre</code>, <code>contacto</code>, <code>pedido</code>.</p>

<h2>Paso 2: el flujo</h2>
<ol>
<li><strong>On form submission</strong> (Form Trigger): armás el formulario ahí mismo, campo por campo, con el mismo nombre que las columnas.</li>
<li><strong>Data table → Insert row</strong>: elegís tu tabla y arrastrás cada respuesta del formulario a su columna.</li>
<li><strong>Telegram → Send a text message</strong>: "Nuevo pedido de " y arrastrás el nombre y el pedido. (El bot se crea igual que en la <a href="recordatorio-diario-telegram-n8n.html">tarea #4</a>.)</li>
</ol>
<p>Probalo completando el formulario de prueba y fijate que aparezca la fila y llegue el aviso. Después tocá <strong>Publish</strong>: recién ahí el link de producción queda activo para tus clientes.</p>

<h2>Errores comunes</h2>
<ul>
<li><strong>Mandaste el link de prueba</strong>: el link "test" solo funciona mientras tenés el editor abierto. A los clientes se les manda el de producción, con el flujo publicado.</li>
<li><strong>Columnas vacías en la tabla</strong>: el nombre del campo del formulario no coincide con el que arrastraste. Revisá el nodo Insert row.</li>
<li><strong>El formulario no abre desde afuera</strong>: si n8n está en tu compu, el link solo funciona en tu red. Para recibir pedidos de clientes necesitás n8n en un servidor o en la nube.</li>
</ul>

<h2>Y después</h2>
<p>Con los pedidos en una tabla, podés pasársela a Claude a fin de mes y pedirle un resumen: cuántos pedidos, qué se vendió más, qué día de la semana entra más trabajo. Todo eso, sin haber copiado nada a mano.</p>
""",
"prompt": "",
"faq": [
("¿Puedo usar Google Sheets en vez de la tabla de n8n?", "Sí, con el nodo de Google Sheets. Necesita conectar tu cuenta de Google, que en el n8n instalado en tu compu lleva un par de pasos más. Para empezar, la tabla de n8n es más simple."),
("¿El formulario puede pedir archivos?", "Sí, el Form Trigger acepta campos de archivo. Guardalos en una carpeta o en tu Drive con otro nodo."),
],
},
{
"slug": "formulas-de-excel-con-ia",
"num": 6,
"titulo": "Cómo pedirle a la IA una fórmula de Excel en castellano (y que funcione)",
"corto": "Fórmulas de Excel con IA",
"desc": "Contale a Claude qué hay en cada columna y qué querés calcular: te da la fórmula en español lista para pegar y te la explica en una línea. Prompt para copiar.",
"video": "RiNdm6Krzr0",
"fecha": "2026-11-26",
"cuerpo": """
<p>Sabés lo que querés calcular ("las ventas de marzo, solo de Pérez"), pero no te acordás si era SUMAR.SI o SUMAR.SI.CONJUNTO, ni dónde iban las comillas. La IA lo resuelve si le explicás la planilla como se la explicarías a un compañero.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>La fórmula escrita en Excel en español (con punto y coma, no coma).</li>
<li>Una explicación de una línea, para que entiendas qué hace.</li>
<li>Si querés, una versión para Google Sheets.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Mirá tu planilla y anotá qué hay en cada columna: "A fecha, B vendedor, C monto".</li>
<li>Pegá el prompt de abajo en Claude y completá los corchetes.</li>
<li>Copiá la fórmula, pegala en la celda y compará el resultado con dos o tres filas hechas a mano.</li>
</ol>

{prompt}

<h2>Ejemplo real</h2>
<p>Para "las ventas de marzo de Pérez" con fecha en A, vendedor en B y monto en C, la respuesta es:</p>
<p><code>=SUMAR.SI.CONJUNTO(C:C;B:B;"Pérez";A:A;"&gt;="&amp;FECHA(2026;3;1);A:A;"&lt;"&amp;FECHA(2026;4;1))</code></p>
<p>Suma la columna C solo en las filas donde B dice Pérez y la fecha cae en marzo.</p>

<h2>Errores comunes</h2>
<ul>
<li><strong>#¿NOMBRE?</strong>: tu Excel está en inglés y la fórmula en español (o al revés). Decile a la IA en qué idioma está tu Excel.</li>
<li><strong>Da 0</strong>: las fechas están guardadas como texto. Pedile a la IA que te diga cómo convertirlas.</li>
<li><strong>Coma o punto y coma</strong>: en Excel en español se separa con punto y coma. Si te da error de fórmula, es lo primero que hay que mirar.</li>
</ul>
""",
"prompt": "Tengo una planilla: [QUÉ HAY EN CADA COLUMNA]. Dame la fórmula de Excel en español para [LO QUE NECESITÁS]. Explicámela en una línea.",
"faq": [
("¿Sirve para Google Sheets?", "Sí. Agregá al final del prompt 'para Google Sheets' y te la da con el formato correcto."),
("¿Tengo que subir la planilla?", "No hace falta. Con describir las columnas alcanza, y así no compartís datos de tu empresa."),
],
},
{
"slug": "resumir-mails-con-ia",
"num": 7,
"titulo": "Cómo resumir 40 mails sin leer en 5 renglones con IA",
"corto": "Resumir 40 mails",
"desc": "Volvés de vacaciones con la bandeja llena: pegá los mails en Claude y en un minuto sabés qué es urgente, qué ignorar y a quién contestar primero.",
"video": "Z9tomnpx1QE",
"fecha": "2026-11-26",
"cuerpo": """
<p>Volvés de vacaciones, o de un día de reuniones, y tenés 40 mails sin leer. Leerlos todos lleva una hora. Pedirle a la IA que te los ordene lleva un minuto, y después leés solo los que importan.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>5 renglones con lo importante.</li>
<li>Una ★ en lo que necesita respuesta hoy.</li>
<li>Qué podés ignorar o archivar sin abrir.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Seleccioná los mails sin leer y copialos. En Gmail o Outlook podés abrirlos en una sola vista, o reenviarte un resumen. Si son pocos, copiá asunto, remitente y primer párrafo de cada uno.</li>
<li>Pegá el prompt de abajo en Claude y después el texto.</li>
<li>Contestá primero los marcados con ★. El resto, cuando puedas.</li>
</ol>

{prompt}

<h2>Cuidado con la información sensible</h2>
<p>Antes de pegar mails de trabajo en una IA, fijate qué permite tu organización. Si hay datos de clientes o de salud, sacalos o usá la versión de IA que tu empresa aprobó.</p>

<h2>Variante para todos los días</h2>
<p>Si lo hacés cada mañana, guardá el prompt en un Proyecto de Claude con instrucciones fijas ("mis prioridades son: jefe, clientes, proveedores"). Así el resumen ya sale ordenado a tu manera.</p>
""",
"prompt": "Te pego mis mails sin leer. Resumilos en 5 renglones: qué es urgente, qué puedo ignorar y a quién contesto primero. Marcá con ★ lo que necesita respuesta hoy.",
"faq": [
("¿Puede leer mi Gmail directamente?", "Claude puede conectarse a Gmail con un conector, si tu cuenta lo permite. Si no, copiar y pegar funciona igual."),
("¿Y si son 200 mails?", "Hacelo por partes de 30 o 40, o pedile primero que los agrupe por remitente."),
],
},
{
"slug": "responder-cliente-enojado-con-ia",
"num": 8,
"titulo": "Cómo contestarle a un cliente enojado con ayuda de la IA (sin sonar a robot)",
"corto": "Cliente enojado",
"desc": "Disculpa, causa y solución con fecha: el prompt para que la IA te escriba una respuesta tranquila y humana, sin 'lamentamos los inconvenientes'.",
"video": "W5FF8xPJcc0",
"fecha": "2026-11-26",
"cuerpo": """
<p>Un cliente te escribe furioso, en mayúsculas, y tu primer impulso es contestarle igual. Ese mail que mandás en caliente casi siempre empeora las cosas. La IA te ayuda a escribir la respuesta que mandarías con la cabeza fría.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Una respuesta corta con tres partes: disculpa, causa y solución con fecha.</li>
<li>Sin frases de manual que enojan más.</li>
<li>Lista para mandar, después de que la revises.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Pegá el mail del cliente en Claude.</li>
<li>Decile qué podés ofrecer de verdad: una fecha, un reintegro, un descuento. Si no lo decís, la IA puede prometer cosas que no podés cumplir.</li>
<li>Usá el prompt de abajo y leé la respuesta en voz alta antes de mandarla.</li>
</ol>

{prompt}

<h2>Por qué funciona</h2>
<p>Un cliente enojado quiere tres cosas: que le den la razón en lo que tiene razón, entender qué pasó y saber cuándo se arregla. "Lamentamos los inconvenientes" no da ninguna de las tres. Una fecha concreta, sí.</p>

<h2>Antes de mandar</h2>
<ul>
<li>Revisá que la solución sea real y que la puedas cumplir.</li>
<li>Si el tema es legal o hay un reclamo formal, consultá antes con quien corresponda.</li>
</ul>
""",
"prompt": "Un cliente me escribió enojado (te lo pego). Puedo ofrecer [LO QUE PODÉS DAR]. Escribí una respuesta corta: disculpa, causa y solución con fecha. Sin frases de robot como 'lamentamos los inconvenientes'.",
"faq": [
("¿Le digo al cliente que lo escribió una IA?", "La respuesta es tuya: vos decidís qué ofrecer y la revisás. La IA te ayuda con la redacción, como un corrector."),
("¿Sirve para WhatsApp?", "Sí. Pedile 'versión corta para WhatsApp' y te la achica."),
],
},
{
"slug": "acta-de-reunion-desde-foto-del-pizarron",
"num": 9,
"titulo": "De la foto del pizarrón al acta de la reunión en 10 segundos (con IA)",
"corto": "Acta desde el pizarrón",
"desc": "Sacale una foto al pizarrón y la IA te arma el acta: decisiones, tareas, responsables y fechas. Y te marca lo que no se lee, en vez de inventarlo.",
"video": "qjGrpYJdLw8",
"fecha": "2026-11-26",
"cuerpo": """
<p>Terminó la reunión, nadie tomó notas y lo único que quedó es el pizarrón lleno de flechas. Antes de que alguien lo borre, sacale una foto: la IA lo convierte en un acta ordenada.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Una tabla con decisiones, tareas, quién y para cuándo.</li>
<li>Las dudas marcadas aparte: lo que no se lee bien no se inventa.</li>
<li>Un texto listo para mandar por mail al equipo.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Sacá la foto de frente, con buena luz y sin reflejos. Si el pizarrón es grande, sacá dos fotos.</li>
<li>Subí la foto a Claude (desde el celular funciona igual) y pegá el prompt de abajo.</li>
<li>Completá las dudas con lo que te acuerdes y mandá el acta antes de que termine el día.</li>
</ol>

{prompt}

<h2>El truco: que no invente</h2>
<p>La letra de pizarrón es difícil de leer, y una IA puede completar lo que no ve. Por eso el prompt termina con "si algo no se lee, marcalo como duda". Es mejor una celda que diga "no se lee" que una fecha inventada.</p>

<h2>Y después</h2>
<p>Pedile "escribí el mail para el equipo con esta acta" y tenés el resumen listo para mandar.</p>
""",
"prompt": "Esta es la foto del pizarrón de la reunión. Armá el acta en una tabla: decisiones, tareas, quién y para cuándo. Si algo no se lee, marcalo como duda: no inventes.",
"faq": [
("¿Funciona con notas en papel?", "Sí, con cualquier foto de texto escrito a mano, siempre que se lea razonablemente."),
("¿Y con la grabación de la reunión?", "También: si tenés la transcripción, pegala con el mismo prompt cambiando 'foto del pizarrón' por 'transcripción'."),
],
},
{
"slug": "nota-de-voz-a-mail-con-ia",
"num": 10,
"titulo": "Cómo convertir una nota de voz en un mail ordenado con IA (en 10 segundos)",
"corto": "Nota de voz → mail",
"desc": "Hablá 3 minutos como te salga y la IA te devuelve el mail: saludo, 3 puntos y qué necesitás que te respondan. Prompt listo para copiar.",
"video": "ed4q3JxeenY",
"fecha": "2026-11-26",
"cuerpo": """
<p>Hay días en que es más rápido explicar algo en voz alta que escribirlo. El problema es que un audio de 3 minutos no se puede mandar a tu jefa. La solución: grabalo igual y que la IA lo convierta en un mail.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Un mail con asunto, saludo y máximo 3 puntos.</li>
<li>Una pregunta final clara: qué necesitás que te respondan.</li>
<li>El tono que elijas: formal o cercano.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Grabá la nota de voz con el celular, sin preocuparte por el orden.</li>
<li>Subí el audio a Claude desde la app, o pegá la transcripción (el celular la hace solo en las notas de voz de WhatsApp o en el grabador).</li>
<li>Pegá el prompt de abajo con el destinatario y el tono.</li>
<li>Leelo una vez y mandalo.</li>
</ol>

{prompt}

<h2>El truco: a quién y en qué tono</h2>
<p>El mismo contenido se escribe distinto para tu jefa, para un cliente o para tu equipo. Si no lo decís, la IA elige un tono neutro que no le queda bien a nadie.</p>

<h2>Errores comunes</h2>
<ul>
<li><strong>El mail sale largo</strong>: pedile "máximo 80 palabras".</li>
<li><strong>Inventa detalles</strong>: si en el audio dijiste "el jueves o el viernes", que no ponga "el jueves". Pedile que deje entre corchetes lo que no está claro.</li>
</ul>
""",
"prompt": "Te paso una nota de voz. Convertila en un mail para [A QUIÉN], tono [FORMAL / CERCANO]: saludo, máximo 3 puntos y qué necesito que me respondan.",
"faq": [
("¿Claude entiende audios?", "En la app podés grabar o subir audio según tu plan y tu país. Si no te aparece la opción, pegá la transcripción: funciona igual."),
("¿Sirve para WhatsApp?", "Sí. Pedile 'versión corta para WhatsApp' al final."),
],
},
{
"slug": "mail-en-ingles-formal-con-ia",
"num": 11,
"titulo": "Cómo escribir un mail en inglés formal sin saber inglés (con IA)",
"corto": "Mail en inglés formal",
"desc": "Escribilo en castellano como te salga y la IA te lo pasa a inglés formal, listo para mandar, con la explicación de cada párrafo para que sepas qué mandás.",
"video": "iYWmEEstBNY",
"fecha": "2026-11-26",
"cuerpo": """
<p>Te piden un mail para alguien de afuera y tu inglés es el del colegio. Los traductores automáticos traducen palabra por palabra y el resultado suena raro. La IA hace otra cosa: reescribe el mensaje como lo escribiría alguien que trabaja en inglés.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>El mail en inglés formal, con saludo y cierre correctos.</li>
<li>La explicación en castellano de cada párrafo.</li>
<li>Si querés, una versión más corta o más cálida.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Escribí el mail en castellano, como te salga. No hace falta que esté prolijo.</li>
<li>Pegá el prompt de abajo con tu texto.</li>
<li>Leé la explicación en castellano: así sabés exactamente qué estás mandando.</li>
</ol>

{prompt}

<h2>El truco: que te lo explique</h2>
<p>Mandar algo que no entendés es arriesgado. Por eso el prompt pide la explicación de cada párrafo: si algo dice más (o menos) de lo que querías, lo ves antes de mandarlo.</p>

<h2>Antes de mandar</h2>
<ul>
<li>Revisá nombres, fechas y cifras.</li>
<li>Si es un tema legal o un contrato, que lo revise alguien que sepa inglés.</li>
</ul>
""",
"prompt": "Pasá este mail a inglés formal, listo para mandar: [TU TEXTO EN CASTELLANO]. Después explicame en castellano qué dice cada párrafo.",
"faq": [
("¿Y para contestar un mail en inglés?", "Pegá el mail que recibiste y pedile: 'explicámelo en castellano y ayudame a contestar'."),
("¿Funciona para otros idiomas?", "Sí: cambiá 'inglés' por el idioma que necesites."),
],
},
{
"slug": "planificar-la-semana-con-ia",
"num": 12,
"titulo": "Cómo planificar la semana con IA: 22 tareas y 5 días",
"corto": "Planificar la semana",
"desc": "Pasale a la IA tus tareas pendientes y tu agenda: te arma la semana día por día, con lo urgente primero y huecos para lo importante. Prompt para copiar.",
"video": "tWS5CF8Lc7Q",
"fecha": "2026-11-26",
"cuerpo": """
<p>Lunes a la mañana: 22 cosas pendientes, reuniones por todos lados y ninguna idea de por dónde empezar. La IA no hace las tareas por vos, pero te ordena la semana en dos minutos.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Un plan de lunes a viernes, con las tareas repartidas.</li>
<li>Lo urgente al principio de la semana.</li>
<li>Bloques libres para lo importante que nunca es urgente.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Hacé la lista de pendientes, una por línea. Si sabés la fecha límite, ponela al lado.</li>
<li>Copiá tu agenda de la semana (o una captura del calendario).</li>
<li>Pegá todo en Claude con el prompt de abajo.</li>
<li>Pasá los bloques a tu calendario.</li>
</ol>

{prompt}

<h2>El truco: horas reales, no ideales</h2>
<p>Si le decís que tenés 8 horas libres por día, te va a armar un plan imposible. Contá las horas que de verdad te quedan entre reuniones, mails e interrupciones. Un plan más corto que se cumple vale más que uno perfecto que no.</p>

<h2>Y el viernes</h2>
<p>Pegale lo que quedó sin hacer y pedile: "pasalo a la semana que viene y decime qué conviene delegar".</p>
""",
"prompt": "Estas son mis tareas pendientes y mi agenda de la semana. Tengo [X] horas libres reales por día. Armá un plan día por día: lo urgente primero y bloques para lo importante.",
"faq": [
("¿Puede ponerlo en mi calendario?", "Si conectás Google Calendar a Claude, puede crear los eventos. Si no, copiás los bloques a mano."),
("¿Sirve para estudiar?", "Sí: cambiá 'tareas' por 'temas' y 'agenda' por 'fechas de examen'."),
],
},
{
"slug": "tareas-programadas-con-ia",
"num": 13,
"titulo": "Tareas programadas con IA: mis 3 «empleados» de 200 dólares por mes",
"corto": "Tareas programadas con IA",
"desc": "Pago 200 dólares por mes de IA y lo anoto como sueldos: tres tareas programadas que trabajan solas a las 03:47, 07:41 y 23:13. Cómo armar la tuya, sin programar.",
"video": "6xzHuoeCBUM",
"fecha": "2026-11-26",
"cuerpo": """
<p>Pago 200 dólares por mes de inteligencia artificial. En mis cuentas no lo anoto como software: lo anoto como sueldos. Porque no es una app que abro cuando me acuerdo, son tareas que corren solas a una hora fija, todos los días, y me dejan el trabajo hecho para que yo solo lo revise.</p>

<h2>Mis 3 «empleados»</h2>
<ul>
<li><b>Radar (03:47):</b> busca los videos que están rindiendo muy por encima de lo normal en mi nicho y me deja un resumen con el gancho, la estructura y una idea propia para cada uno.</li>
<li><b>Novedades (07:41):</b> junta las novedades de IA del día y escribe el guion de un video corto, que queda programado para la tarde.</li>
<li><b>Turno noche (23:13):</b> programa los videos de mi otro canal y fija los comentarios.</li>
</ul>
<p>Ninguno publica nada por su cuenta sin que quede registrado: todo queda programado o anotado para que yo lo apruebe.</p>

<h2>Cómo armar la tuya, paso a paso</h2>
<ol>
<li>Elegí una tarea que hacés todos los días igual (revisar algo, juntar datos, mandar un resumen).</li>
<li>Escribila como si se la explicaras a alguien nuevo: qué mira, qué hace y dónde deja el resultado.</li>
<li>Pegá el prompt de abajo en Claude con tu hora y tu tarea.</li>
<li>Probala una vez a mano antes de dejarla programada.</li>
</ol>

{prompt}

<h2>El truco: que te deje el trabajo para aprobar</h2>
<p>La tarea programada no tiene que decidir por vos. Pedile que deje el resultado en un lugar fijo (un documento, una lista, un borrador) y que te avise. Vos aprobás en dos minutos lo que antes te llevaba una hora.</p>

<h2>Antes de pagar</h2>
<p>No hace falta empezar con 200 dólares. Arrancá con una sola tarea y la herramienta más barata que te sirva; si te ahorra tiempo de verdad, recién ahí sumá la segunda.</p>""",
"prompt": "Quiero que una tarea se haga sola todos los días a las [HORA]: [QUÉ TIENE QUE HACER]. Decime qué herramienta usar y armame el paso a paso, sin programar.",
"faq": [
("¿Necesito saber programar?", "No. Hoy varias herramientas (Claude, n8n, Zapier) dejan programar tareas a una hora fija con instrucciones en castellano."),
("¿Qué pasa si se equivoca?", "Por eso conviene que deje todo para aprobar y no publique ni mande nada solo hasta que confíes en el resultado."),
],
},
{
"slug": "resumir-pdf-largo-con-ia",
"num": 14,
"titulo": "Cómo resumir un PDF largo con IA: 80 páginas en una carilla",
"corto": "Resumir un PDF largo",
"desc": "Subí el PDF a la IA y pedile un resumen de una carilla con las decisiones, los números y lo que te toca a vos. Con el prompt para copiar y cómo chequear que no invente.",
"video": "Z9tomnpx1QE",
"fecha": "2026-11-26",
"cuerpo": """
<p>Te mandan un informe de 80 páginas y te piden "una opinión para mañana". Leerlo entero te lleva la tarde. La IA lo lee en un minuto y te deja una carilla con lo que importa, y vos usás tu tiempo en pensar, no en subrayar.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Un resumen de una carilla, en castellano simple.</li>
<li>Las decisiones, fechas y números importantes, cada uno con la página donde aparece.</li>
<li>Una lista corta de lo que te toca hacer a vos (o a tu área).</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Abrí Claude y adjuntá el PDF con el clip. Si es un PDF escaneado (una foto de papel), igual funciona, pero revisá más los números.</li>
<li>Pegá el prompt de abajo y completá para quién es el resumen.</li>
<li>Leé el resumen y abrí el PDF en dos o tres de las páginas que te cita, para confirmar.</li>
<li>Si algo no queda claro, preguntale ahí mismo: "¿qué dice exactamente la página 34 sobre el presupuesto?".</li>
</ol>

{prompt}

<h2>El truco: pedile las páginas</h2>
<p>Pedir el número de página de cada dato cambia todo. Te deja comprobar en segundos lo importante y, si la IA no encuentra dónde lo dice, es señal de que lo dedujo y no está en el documento.</p>

<h2>Errores comunes</h2>
<ul>
<li><b>Pedir "un resumen" a secas.</b> Te devuelve un índice comentado. Decile para quién es y qué decisión tiene que tomar esa persona.</li>
<li><b>Creerle los números sin mirar.</b> Los montos y porcentajes, chequealos siempre en el original antes de reenviarlos.</li>
<li><b>Subir documentos confidenciales sin preguntar.</b> Si es un contrato o datos de personas, fijate primero qué permite tu empresa.</li>
</ul>

<p>En este video te muestro una tarea parecida: resumir 40 mails en 5 renglones. El método es el mismo.</p>
""",
"prompt": "Te adjunto un PDF de [N] páginas. Resumilo en una carilla para [quién lo va a leer], que tiene que decidir [qué decisión]. Incluí: de qué se trata en 3 renglones, las decisiones y fechas importantes, los números clave y qué nos toca hacer a nosotros. Al lado de cada dato poné la página. Si algo no está en el documento, no lo inventes: decime que no aparece.",
"faq": [
("¿Hay un límite de páginas?", "Depende de la herramienta y del plan. Si el PDF es muy largo y te da error, partilo en dos o tres partes y pedile un resumen de cada una, y después uno final."),
("¿Sirve para PDFs en inglés?", "Sí. Pedile que el resumen te lo haga en castellano, y que deje en inglés los términos técnicos para que los puedas buscar en el original."),
],
},
{
"slug": "planilla-de-gastos-desde-tickets-con-ia",
"num": 15,
"titulo": "Planilla de gastos desde fotos de tickets con IA (sin tipear nada)",
"corto": "Gastos desde tickets",
"desc": "Sacale foto a los tickets y la IA te arma la tabla de gastos con fecha, comercio, categoría e importe, lista para pegar en Excel o Google Sheets. Prompt para copiar.",
"video": "qjGrpYJdLw8",
"fecha": "2026-11-26",
"cuerpo": """
<p>Fin de mes, rendición de gastos, y una pila de tickets arrugados en el cajón. Tipearlos uno por uno es la tarea más aburrida de la oficina. Con la IA alcanza con sacarles foto.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Una tabla con una fila por ticket: fecha, comercio, categoría, importe y moneda.</li>
<li>El total por categoría.</li>
<li>Una lista de los tickets que no se leían bien, para revisarlos a mano.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Poné los tickets sobre una mesa con buena luz y sacales foto. Podés poner varios en una misma foto si no se tapan.</li>
<li>Subí las fotos a Claude (o a la IA que uses) y pegá el prompt de abajo con tus categorías.</li>
<li>Copiá la tabla y pegala en Excel o Google Sheets: cada columna cae en su lugar.</li>
<li>Hacé la suma con una fórmula de la planilla, no con la del chat.</li>
</ol>

{prompt}

<h2>El truco: que te marque lo dudoso</h2>
<p>Los tickets térmicos se borran y la IA puede leer un 3 como un 8. Por eso el prompt le pide una columna "¿seguro?" con un "revisar" cuando no lee bien. Así mirás a mano solo esos dos o tres, y no los treinta.</p>

<h2>Cuidado</h2>
<ul>
<li><b>El total, en la planilla.</b> Pedile la tabla, pero que la cuenta final la haga una fórmula (=SUMA). Es más fácil de revisar y de auditar.</li>
<li><b>Guardá los originales.</b> Para una rendición oficial o para impuestos, la foto no reemplaza al comprobante que te pidan.</li>
<li><b>Datos personales.</b> Si en el ticket aparece tu número de documento o el de tu tarjeta, tapalo antes de sacar la foto.</li>
</ul>

<p>En este video te muestro una tarea parecida: pasar la foto del pizarrón a un acta ordenada. La idea es la misma: foto, prompt y listo.</p>
""",
"prompt": "Te paso fotos de tickets de gastos. Armame una tabla con estas columnas: fecha, comercio, categoría, importe, moneda y ¿seguro?. Usá solo estas categorías: [viáticos, comida, transporte, insumos, otros]. Si no leés bien un dato, escribí 'revisar' en la última columna y no lo adivines. Al final dame el total por categoría.",
"faq": [
("¿Lee tickets escritos a mano?", "Muchas veces sí, si la letra se entiende. Igual son los que más conviene revisar: pedile que los marque con 'revisar'."),
("¿Me puede dar directamente el archivo de Excel?", "Claude puede generar un archivo para descargar, pero copiar la tabla y pegarla en tu planilla de siempre suele ser más rápido y te deja usar tu formato de rendición."),
],
},
{
"slug": "preparar-reunion-dificil-con-el-jefe-con-ia",
"num": 16,
"titulo": "Cómo preparar una reunión difícil con tu jefe usando IA",
"corto": "Reunión difícil con el jefe",
"desc": "Pedir un aumento, decir que no llegás con un proyecto o plantear un problema: la IA te ayuda a ordenar los argumentos y a ensayar las preguntas incómodas antes de entrar. Prompt para copiar.",
"video": "W5FF8xPJcc0",
"fecha": "2026-11-26",
"cuerpo": """
<p>Tenés que pedirle a tu jefe algo incómodo: más tiempo para un proyecto, un cambio de tareas, una revisión de sueldo. Lo pensás toda la semana y, cuando entrás, te olvidás de la mitad. La IA no va a la reunión por vos, pero te deja entrar preparado.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Tu pedido en una sola frase clara.</li>
<li>Tres argumentos ordenados, con hechos concretos.</li>
<li>Las cinco preguntas o objeciones más probables, con una respuesta para cada una.</li>
<li>Un ensayo: la IA hace de tu jefe y vos practicás.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Escribí en un borrador qué querés pedir y por qué, sin ordenar nada. Sumá hechos: fechas, resultados, cuánto trabajo tenés.</li>
<li>Pegalo en Claude con el prompt de abajo.</li>
<li>Cuando te devuelva el plan, escribile: "Ahora hacé de mi jefe. Haceme las preguntas de a una y esperá mi respuesta".</li>
<li>Al final pedile una devolución: qué respuesta tuya sonó débil y cómo decirla mejor.</li>
</ol>

{prompt}

<h2>El truco: ensayá la peor respuesta</h2>
<p>Pedile que el jefe del ensayo sea duro y te diga que no. Si ya practicaste qué contestar a un "no hay presupuesto" o a un "ahora no es el momento", en la reunión real no te agarra desprevenido.</p>

<h2>Cuidado</h2>
<ul>
<li><b>No le leas un guion.</b> Usá lo que preparaste como puntos de apoyo, no como un texto para recitar.</li>
<li><b>Los hechos los ponés vos.</b> La IA ordena y redacta, pero no conoce tu empresa: no le pidas que invente logros o números.</li>
<li><b>Cuidá los datos de otros.</b> Si hablás de compañeros, no hace falta poner nombres.</li>
</ul>

<p>En este video te muestro una tarea parecida: responder a un cliente enojado sin frases de robot. El método es el mismo: contexto, tono y que te lo ordene.</p>
""",
"prompt": "Tengo una reunión con mi jefe para [lo que quiero pedir o plantear]. Contexto: [situación, fechas, resultados concretos]. Armame: mi pedido en una frase, tres argumentos ordenados con hechos, y las cinco objeciones más probables de mi jefe con una respuesta corta para cada una. Tono: respetuoso y firme, sin sonar a reclamo.",
"faq": [
("¿Sirve para una entrevista de trabajo?", "Sí. Cambiá 'mi jefe' por 'el entrevistador' y pegale la descripción del puesto: te arma las preguntas probables y podés ensayarlas igual."),
("¿Y si la reunión es por mail?", "Pedile que, con los mismos argumentos, te escriba un mail corto. Leelo en voz alta antes de mandarlo: si no suena a vos, cambiale las palabras."),
],
},
{
"slug": "descripcion-de-puesto-con-ia",
"num": 17,
"titulo": "Cómo escribir una descripción de puesto con IA en 5 minutos",
"corto": "Descripción de puesto",
"desc": "Contale a la IA qué hace la persona en el día a día y te escribe la descripción del puesto: tareas, requisitos, lo deseable y el aviso para publicar. Prompt para copiar.",
"video": "qNwSzF7oj5o",
"fecha": "2026-11-26",
"cuerpo": """
<p>Se va alguien del equipo, o entra presupuesto para una persona nueva, y te piden "pasame la descripción del puesto para Recursos Humanos". Empezar de cero en una hoja en blanco cuesta. Contarle a la IA qué hace esa persona, no.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Una descripción del puesto con objetivo, tareas principales, requisitos y lo deseable.</li>
<li>Una versión corta para publicar como aviso.</li>
<li>Tres preguntas para la entrevista, pensadas para ese puesto.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Anotá, como te salga, qué hace la persona en una semana normal: tareas, con quién trabaja, qué herramientas usa.</li>
<li>Separá lo que tiene que saber sí o sí de lo que estaría bueno que sepa.</li>
<li>Pegá todo en Claude con el prompt de abajo.</li>
<li>Pasáselo a alguien que hace ese trabajo hoy y preguntale qué falta.</li>
</ol>

{prompt}

<h2>El truco: tareas reales, no adjetivos</h2>
<p>"Proactivo, dinámico y con ganas de crecer" no le dice nada a nadie. Pedile que cada tarea empiece con un verbo y sea algo que se pueda ver: "atender 20 consultas por día por mail", "cerrar la caja del mes". Así el aviso atrae a la gente correcta.</p>

<h2>Cuidado</h2>
<ul>
<li><b>Requisitos que discriminan.</b> Edad, género, estado civil o "buena presencia" no van. El prompt ya se lo pide, pero revisalo igual.</li>
<li><b>No inflar requisitos.</b> Si pedís cinco años de experiencia para un puesto inicial, no se postula nadie. Dejá como obligatorio solo lo indispensable.</li>
<li><b>Revisión final de RR. HH.</b> Cada empresa tiene su formato y sus reglas: usá el texto de la IA como borrador.</li>
</ul>

<p>En este video te muestro una tarea parecida: armar el manual de la tarea que solo vos sabés hacer. También parte de contarle a la IA cómo es el trabajo de verdad.</p>
""",
"prompt": "Escribí la descripción del puesto de [nombre del puesto] en [tipo de empresa]. Esto es lo que hace en una semana normal: [tareas]. Indispensable: [lo que tiene que saber]. Deseable: [lo que suma]. Incluí: objetivo del puesto en 2 renglones, tareas principales que empiecen con un verbo, requisitos, deseables, una versión corta para publicar y 3 preguntas para la entrevista. No incluyas requisitos de edad, género ni estado civil.",
"faq": [
("¿Puedo usarla para actualizar mi propio puesto?", "Sí, y conviene: muchas veces la descripción oficial quedó vieja. Pegale lo que hacés hoy y comparala con la que figura."),
("¿La puedo pedir en inglés?", "Sí: pedile la misma descripción en inglés al final. Si la vas a publicar, que la revise alguien que maneje bien el idioma."),
],
},
{
"slug": "presupuesto-desde-lista-de-precios-con-ia",
"num": 18,
"titulo": "Cómo armar un presupuesto desde una lista de precios con IA",
"corto": "Presupuesto desde una lista de precios",
"desc": "Pegale a la IA tu lista de precios y el pedido del cliente: te arma el presupuesto con cantidades, subtotales y condiciones, listo para mandar. Con cómo chequear las cuentas.",
"video": "0BUKGR9WPy8",
"fecha": "2026-11-26",
"cuerpo": """
<p>Un cliente te pide "pasame precio por esto, esto y aquello" y vos tenés la lista de precios en una planilla de 300 renglones. Buscar cada producto, multiplicar y armar el documento lleva media hora. La IA lo arma en dos minutos, y vos solo revisás.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Un presupuesto con cada producto, cantidad, precio unitario y subtotal.</li>
<li>El total, con el descuento o el impuesto que corresponda.</li>
<li>Las condiciones: validez, forma de pago y plazo de entrega.</li>
<li>Una lista de lo que el cliente pidió y no está en tu lista de precios.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Exportá o copiá la lista de precios (de Excel, Google Sheets o un PDF) y pegala en Claude.</li>
<li>Pegá el pedido del cliente tal como te llegó: mail, WhatsApp o nota.</li>
<li>Usá el prompt de abajo con tus condiciones de siempre.</li>
<li>Pasá el resultado a tu planilla o plantilla de presupuesto y dejá que las fórmulas hagan las cuentas.</li>
</ol>

{prompt}

<h2>El truco: que no adivine productos</h2>
<p>El cliente escribe "cable largo" y en tu lista hay cuatro cables. Si no se lo pedís, la IA elige uno. Con el prompt de abajo, cuando hay dudas te pregunta o lo pone en la lista de "a confirmar", y vos decidís.</p>

<h2>Errores comunes</h2>
<ul>
<li><b>Mandar el presupuesto sin revisar las cuentas.</b> La IA puede equivocarse al multiplicar. Antes de enviarlo, pasá las cantidades y precios a la planilla y que la fórmula calcule el total.</li>
<li><b>Lista de precios vieja.</b> Si actualizaste precios, pegá la lista nueva cada vez: no confíes en la que le pasaste la semana pasada.</li>
<li><b>Olvidar la validez.</b> Con precios que cambian seguido, poné siempre hasta qué fecha vale el presupuesto.</li>
</ul>

<p>En este video te muestro una tarea parecida: pedirle a la IA la fórmula de Excel en castellano. Te sirve para que la planilla haga las cuentas del presupuesto.</p>
""",
"prompt": "Te paso mi lista de precios y el pedido de un cliente. Armá un presupuesto con: producto, cantidad, precio unitario y subtotal, y el total con [descuento o impuesto]. Condiciones: validez [X días], pago [forma de pago], entrega [plazo]. Usá solo productos que estén en la lista: si algo del pedido no está o hay más de una opción, no elijas vos, ponelo aparte en 'a confirmar'.",
"faq": [
("¿Puede leer la lista de precios en PDF?", "Sí, si el PDF tiene el texto (no es una foto). Si es una lista muy larga, pegale solo la parte de los productos del pedido para que no se mezcle."),
("¿Me lo deja con mi logo?", "El chat te da el texto y la tabla. Para el logo y el formato, pegalo en tu plantilla de siempre de Word, Google Docs o Excel."),
],
},
{
"slug": "grafico-desde-excel-con-ia",
"num": 19,
"titulo": "Cómo hacer un gráfico desde tu Excel con IA (para la reunión, en minutos)",
"corto": "Gráfico desde el Excel para la reunión",
"desc": "Pasale tu planilla de ventas a la IA y te arma el gráfico de ventas por mes, con el mejor mes marcado y la frase para la diapositiva. Con cómo chequear que los números estén bien.",
"video": "5-OjPDoiyfE",
"fecha": "2026-11-27",
"cuerpo": """
<p>Tenés una planilla con 300 filas de ventas y tu jefe quiere "un gráfico para la reunión". Armar la tabla dinámica, elegir el tipo de gráfico y pensar qué decir lleva un rato. La IA lo hace en un par de minutos, y vos solo revisás.</p>

<h2>Qué vas a tener al final</h2>
<ul>
<li>Las ventas sumadas por mes (o por vendedor, o por producto: lo que pidas).</li>
<li>Un gráfico de barras con el mejor mes marcado.</li>
<li>Una frase con la conclusión, lista para poner en la diapositiva.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Subí el archivo de Excel (o el CSV) a Claude. Si la planilla tiene datos sensibles, borrá antes las columnas que no hacen falta (nombres de clientes, por ejemplo).</li>
<li>Usá el prompt de abajo. Si querés otro corte, cambiá "por mes" por "por vendedor" o "por producto".</li>
<li>Descargá el gráfico como imagen o pedile la tabla resumida para armar el gráfico en tu Excel o en tus diapositivas.</li>
<li>Chequeá un total a mano antes de presentarlo (ver abajo).</li>
</ol>

{prompt}

<h2>El truco: pedile la conclusión, no solo el dibujo</h2>
<p>Un gráfico solo no dice nada en una reunión. Si le pedís también "qué tengo que contar", te devuelve la frase (por ejemplo, cuál fue el mejor mes y cuánto creció contra el primero) y llegás con el mensaje armado.</p>

<h2>Errores comunes</h2>
<ul>
<li><b>Presentar sin chequear.</b> Elegí un mes y sumalo vos en Excel con =SUMA o un filtro: si coincide con lo que dice la IA, vas tranquilo.</li>
<li><b>Fechas mal leídas.</b> Si tu planilla usa día/mes y la IA lo toma como mes/día, los meses salen cambiados. Decile el formato de fecha en el prompt.</li>
<li><b>Filas de totales dentro de los datos.</b> Si la planilla ya tiene una fila de "Total", sacala o avisale: si no, la suma sale duplicada.</li>
</ul>
""",
"prompt": "Te paso mi planilla de ventas (Excel). Las fechas están en formato [día/mes/año]. Armá un gráfico de barras de ventas por mes, marcá el mejor mes y decime en una frase qué conclusión tengo que contar en la reunión. Mostrame también la tabla con el total de cada mes para que pueda chequearla.",
"faq": [
("¿Necesito saber hacer tablas dinámicas?", "No. Le subís el archivo y le pedís el resumen en castellano. Si después querés el gráfico dentro de tu Excel, pedile la tabla resumida y la pegás."),
("¿Sirve con Google Sheets?", "Sí: descargá la hoja como Excel o CSV (Archivo → Descargar) y subí ese archivo."),
],
},
{
"slug": "radar-de-videos-virales-con-ia",
"num": 20,
"titulo": "Cómo armar un radar de videos virales con IA (que trabaja de madrugada)",
"corto": "Radar de videos virales de tu nicho",
"desc": "Una tarea programada que revisa a los creadores que seguís, se queda con los videos que hicieron más de 3 veces su promedio y te deja el gancho, la estructura y por qué pegaron.",
"video": None,
"fecha": "2026-11-27",
"cuerpo": """
<p>Si hacés videos, mirar todos los días qué está funcionando en tu nicho te come una hora. Yo tengo una tarea programada que lo hace sola antes de las 4 de la mañana: revisa a los creadores que sigo y me deja un reporte. Esta semana encontró un video que hizo 713 veces el promedio de su creador.</p>

<h2>Qué hace el radar</h2>
<ul>
<li>Revisa los últimos videos de una lista de cuentas que vos elegís.</li>
<li>Compara las vistas de cada video con el promedio (la mediana) de ese creador.</li>
<li>Se queda solo con los que hicieron 3 veces o más su promedio (y un mínimo de vistas, para no perseguir ruido).</li>
<li>De cada uno anota la primera frase literal, la estructura en 5 pasos, por qué cree que funcionó y una idea para tu canal.</li>
</ul>

<h2>Paso a paso</h2>
<ol>
<li>Hacé la lista: 10 a 20 cuentas de tu nicho, en una sola red para empezar.</li>
<li>Elegí la hora. De madrugada está bien: a la mañana ya tenés el reporte.</li>
<li>Usá el prompt de abajo en una tarea programada (en Claude, \"Scheduled tasks\"; también sirve cualquier herramienta que corra un prompt todos los días).</li>
<li>Leé el reporte y quedate con una idea por día. Una sola.</li>
</ol>

{prompt}

<h2>El truco: comparar contra el promedio del creador, no contra las vistas</h2>
<p>Un video con 50.000 vistas de una cuenta que siempre hace 50.000 no te dice nada. Uno con 20.000 de una cuenta que hace 2.000 sí: ese formato funcionó por algo. Por eso el filtro es \"3 veces su promedio\" y no \"más de X vistas\".</p>

<h2>Errores comunes</h2>
<ul>
<li><b>Copiar el video.</b> El radar sirve para entender el formato (el gancho, el ritmo, el cierre). Los personajes, los textos y las ideas de otros no se copian: lo contás con tus datos.</li>
<li><b>Seguir demasiadas cuentas.</b> Con 50 cuentas el reporte se vuelve largo y no lo leés. Empezá con pocas.</li>
<li><b>Creerle todos los números.</b> Si algo te sorprende, abrí el video y chequealo antes de usarlo.</li>
</ul>
""",
"prompt": "Todos los días a las [HORA], revisá los últimos videos de estas cuentas: [LISTA]. Decime cuáles hicieron más de 3 veces su promedio de vistas y, de cada uno, la primera frase, la estructura en 5 pasos y por qué creés que funcionó.",
"faq": [
("¿Necesito programar?", "No. Es un prompt en una tarea programada. Si la herramienta no puede entrar a una red social, pegale vos los links de la semana y pedile el mismo análisis."),
("¿Cada cuánto conviene correrlo?", "Una vez por día alcanza. Más seguido solo te trae los mismos videos."),
],
},
]
