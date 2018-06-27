#-*-coding:utf-8-*-
import smtplib
import email.message

email_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
   <title>Jorge Luis Ch&aacute</title>
   <style type="text/css">
    a {color: #d80a3e;}
  body, #header h1, #header h2, p {margin: 0; padding: 0;}
  #main {border: 1px solid #cfcece;}
  img {display: block;}
  #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
  #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
  #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
  h5 {margin: 0 0 0.8em 0;}
    h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
  p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
   </style>
</head>
 
<body>
 
 
<table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
<table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p><a href="https://kubos777.github.io/PersonalWebSite/index.html">Mi pagina personal</a></p>
      </td>
    </tr>
  </table>
 
<table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
    <tr>
      <td>
        <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
          <tr>
            <td width="570" align="center"  bgcolor="#50C2F4"><h1>Jorge Chavez</h1></td>
          </tr>
          <tr>
            <td width="570" align="right" bgcolor="#50C2F4"><p>Junio 2018</p></td>
          </tr>
        </table>
      </td>
    </tr>
 
    <tr>
      <td>
        <table id="content-3" cellpadding="0" cellspacing="0" align="center">
          <tr>
              <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
              <img src="https://www.linuxadictos.com/wp-content/uploads/python-logo.jpg" width="250" height="150"/>
            </td>
              <td width="15"></td>
            <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                <img src="https://www.aprenderpython.net/wp-content/uploads/2017/08/django-300x300.png" width ="250" height="150" />
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table id="content-4" cellpadding="0" cellspacing="0" align="center">
          <tr>
            <td width="200" valign="top">
              <h5>Aprender Python</h5>
              <p>Deberia ser esencial que cualquier persona aprenda a programar en 
              cualquier lenguaje de programacion. Python por ejemplo es la mejor opcion</p>
            </td>
            <td width="15"></td>
            <td width="200" valign="top">
              <h5>Django</h5>
              <p>Un super framework para darle vida a tus sitios web, rapido, seguro y lo mejor
              esta hecho con python.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
     
 
  </table>
  <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p>El mejor curso de Python, los mejores instructores</p>
        <p><a href="https://github.com/kubos777">GitHub</a> | <a href="https://www.facebook.com/jorge.chavez.165">Facebook</a> | <a href="https://www.instagram.com/kubos777">Instagram</a></p>
      </td>
    </tr>
  </table><!-- top message -->
</td></tr></table><!-- wrapper -->
 
</body>
</html>

"""
try:
  msg = email.message.Message()
  msg['Subject'] = 'El mejor curso de tu vida'

  msg['From'] = 'cursopython.proteco@gmail.com'
  msg['To'] = 'jorgechavez.proteco@gmail.com'
  password = "python.isCool"
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(email_content)
   
  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
   
  # Login Credentials for sending the mail
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string()) 
except UnicodeEncodeError: 
  print("Error de codificación.")
else:
  print("Mensaje enviado!")
