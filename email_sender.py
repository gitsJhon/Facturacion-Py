import os  # Para trabajar con variables de entorno
from dotenv import load_dotenv  # Para cargar variables desde un archivo .env
from email.message import EmailMessage  # Para crear el mensaje de correo electrónico
import ssl  # Para configurar la conexión segura
import smtplib  # Para enviar correos usando el protocolo SMTP

def send_email(archivo, destinatario, nombre_destinatario):
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Obtener la contraseña almacenada como variable de entorno
    password = os.getenv('PASSWORD')  # Asegúrate de tener una variable PASSWORD en tu archivo .env

    # Dirección de correo del remitente
    email_sender = "Tu correo"

    # Crear un mensaje de correo electrónico
    em = EmailMessage()
    em["From"] = email_sender  # Remitente
    em["To"] = destinatario  # Destinatario del correo
    em["Subject"] = f"Factura para {nombre_destinatario}"  # Asunto del correo

    # Contenido del correo
    em.set_content(f"Hola {nombre_destinatario},\n\nAqui esta tu factura.\n\nSaludos.")  # Texto del cuerpo del correo
    # Adjuntar el archivo
    try:
        with open(archivo, "rb") as f:
            # Leer el archivo y adjuntarlo al correo
            em.add_attachment(
                f.read(),
                maintype="application",  # Tipo de contenido principal
                subtype="octet-stream",  # Subtipo para archivos binarios
                filename=os.path.basename(archivo)  # Nombre del archivo adjunto
            )
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró. Por favor, verifica la ruta.")

    # Crear un contexto SSL para establecer una conexión segura
    context = ssl.create_default_context()

    # Conexión al servidor SMTP usando SSL
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            # Autenticación en el servidor usando las credenciales del remitente
            smtp.login(email_sender, password)

            # Enviar el correo
            smtp.send_message(em)
            print(f"Correo enviado exitosamente a {destinatario}.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
