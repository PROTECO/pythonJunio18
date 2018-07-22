#Modulos necesarios
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
# Parámetros del script
remitente = 'cursopython.proteco@gmail.com'
#destinatarios = ['jorgechavez.proteco@gmail.com']
destinatarios = ["jorgechavez.proteco@gmail.com",
           "ae@ciencias.unam.mx",
           "alejandracastrejong@gmail.com",
           "mzl@ciencias.unam.mx",
           "nicollegamao@gmail.com",
           "jrggsnorf@gmail.com",
           "mbarrerav99@gmail.com",
           "joandyramirez1@gmail.com",
           "jazz05d@gmail.com",
           "sandravzch@gmail.com",
           "oasis26v@gmail.com",
           "rios.luisfrancisco@gmail.com",
           "auro3194@gmail.com",
           "mebla07@gmail.com",
           "paulina.nunez.ilp@gmail.com",
           "raul.990527@gmail.com"]

asunto = 'Código de bases de datos'
cuerpo = ''' Aquí se encuentran los códigos vistos el Miércoles y Jueves: https://github.com/PROTECO/pythonJunio18/tree/master/Intermedio/Jueves. 
Recuerden terminar las opciones que faltan :) Bonita Tarde.
Jorge Chávez!'''
password = 'python.isCool'
#ruta_adjunto = 'unam.jpg'
#nombre_adjunto = 'unam.jpg'
ruta_adjunto = "../Jueves/BasesDeDatos/alumnoCurso.py"
nombre_adjunto = "../Jueves/BasesDeDatos/alumnoCurso.py"
#ruta_adjunto = "libroRandomdeIA.pdf"
#nombre_adjunto = "libroRandomdeIA.pdf"

# Creamos el objeto mensaje
mensaje = MIMEMultipart()
 
# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto
 
# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))
 
# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')
 
# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)
 
# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
 
# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login(remitente,password)

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos la conexión
sesion_smtp.quit()