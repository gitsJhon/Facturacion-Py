# Facturacion-Py
Desarrollo para una veterinaria local de mi comunidad, esta es una versión con funcionalidades sin mostrar información de la veterinaria como empresa

# Esta app la desarrolle basandome en una del canal Pildora de Programacion, adaptandola a las necesidades de mi cliente
# Instrucciones para personalizar:

#Scritps:
        Esta app usa credenciales de Gmail para enviar correos, por lo que dentro del codigo borre las mias propias,
        para obtener tus propias credenciales, activa dentro de tu cuenta de Gmail la verificacion en dos paso y 
        dirigite al apartado de claves para aplicaciones, ahi obtendras la clave que usara esta app para enviar
        correos, la cual debera ser insertada en el archivo ".env", ademas deberas especificar tu correo en el arhcivo
        "email_sender.py"

#Plantilla de word

A continuacion, explicare como debes manejar la plantilla de word para tus facturas:
1. Colocar de manera correcta las claves:
        Las claves de busqueda dentro del archivo deberan ser escritas dentro de campos de textos, copialas de un editor de texto
        y pegalas en el lugar correspondiente sin formato de texto, esto impedira que Word divida las claves entre archivos .XML
2. Extraer archivos necesarios
        Una vez este lista tu plantilla, debes pasar tu archivo .DOCX a .ZIP y descomprime este, dentro de este encontraras una carpeta
        llamada Word, en ella encontraras el archivo "document.XML" el cual contiene las claves que definiste para la busqueda, este
        archivo muevelo a la raiz de proyecto
