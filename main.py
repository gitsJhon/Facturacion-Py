import flet as ft
import shutil
import zipfile
import os
from email_sender import send_email
#Estructura del encabezado
fecha_facturacion = ft.TextField(label='Fecha Facturación',
                            hint_text="Dia - Mes - Años", 
                            width=300)

correo_factura = ft.TextField(label='Correo del cliente',
                            hint_text='Correo del cliente', 
                            width=300)

nombre_cliente = ft.TextField(label='Nombre Cliente',
                            hint_text='Nombre Cliente', 
                            width=300)

direccion_cliente = ft.TextField(label='Dirección Cliente',
                            hint_text='Dirección Cliente', 
                            width=300)

#Estructura items
item_name_1 = ft.TextField(label='Item 1',
                            hint_text='Item 1', 
                            width=300)

item_name_2 = ft.TextField(label='Item 2',
                            hint_text='Item 2', 
                            width=300)
item_name_3 = ft.TextField(label='Item 3',
                            hint_text='Item 3', 
                            width=300)
item_name_4 = ft.TextField(label='Item 4',
                            hint_text='Item 4', 
                            width=300)
item_name_5 = ft.TextField(label='Item 5',
                            hint_text='Item 5', 
                            width=300)
item_name_6 = ft.TextField(label='Item 6',
                            hint_text='Item 6', 
                            width=300)
item_name_7 = ft.TextField(label='Item 7',
                            hint_text='Item 7', 
                            width=300)
#Cantidad de items
quantity_item_1 = ft.TextField(label='Cantidad Item 1',
                            value='0', 
                            text_align='center',
                            width=150)

quantity_item_2 = ft.TextField(label='Cantidad Item 2',
                            value='0', 
                            text_align='center',
                            width=150)
quantity_item_3 = ft.TextField(label='Cantidad Item 3',
                            value='0', 
                            text_align='center',
                            width=150)
quantity_item_4 = ft.TextField(label='Cantidad Item 4',
                            value='0', 
                            text_align='center',
                            width=150)
quantity_item_5 = ft.TextField(label='Cantidad Item 5',
                            value='0', 
                            text_align='center',
                            width=150)
quantity_item_6 = ft.TextField(label='Cantidad Item 6',
                            value='0', 
                            text_align='center',
                            width=150)
quantity_item_7 = ft.TextField(label='Cantidad Item 7',
                            value='0', 
                            text_align='center',
                            width=150)
#Precio de cada item por unidad
price_item_1 = ft.TextField(label='Precio Item 1',
                            value='0', 
                            text_align='center',
                            width=150)

price_item_2 = ft.TextField(label='Precio Item 2',
                            value='0', 
                            text_align='center',
                            width=150)
price_item_3 = ft.TextField(label='Precio Item 3',
                            value='0', 
                            text_align='center',
                            width=150)
price_item_4 = ft.TextField(label='Precio Item 4',
                            value='0', 
                            text_align='center',
                            width=150)
price_item_5 = ft.TextField(label='Precio Item 5',
                            value='0', 
                            text_align='center',
                            width=150)
price_item_6 = ft.TextField(label='Precio Item 6',
                            value='0', 
                            text_align='center',
                            width=150)
price_item_7 = ft.TextField(label='Precio Item 7',
                            value='0', 
                            text_align='center',
                            width=150)
#Otros

checbox = ft.Checkbox(
                        label="Enviar factura al correo",
                        value= False
                    )

dialogo = ft.AlertDialog(title=ft.Text("Factura Generada"), 
                         on_dismiss=lambda e: print("Cerrado") )

def generar_factura(datos):
    shutil.copytree('plantilla','documento_tmp')

    with open('document.xml', 'r') as file:
        data = file.read()
        for key, value in datos.items():
            data = data.replace(key, value)

    with open('documento_tmp/word/document.xml', 'w') as file:
        file.write(data)
    archivo = f"{nombre_cliente.value}_{fecha_facturacion.value}.docx"
    with zipfile.ZipFile(archivo, 'w') as zipf:
        for root, dirs, files in os.walk('documento_tmp'):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                           'documento_tmp'))        
    shutil.rmtree('documento_tmp')
            

def main(page: ft.Page):
    page.scroll = "none"
    page.window_width = 700
    titulo = ft.Text('Creación de Factura', style=ft.TextThemeStyle.HEADLINE_LARGE)

    def obtener_datos(e):
        data_factura = {
            # cliente info
            '%FECHA%' : fecha_facturacion.value,
            '%CORREO%' : correo_factura.value,
            '%NOMBRE%' : nombre_cliente.value,
            '%DIRECCION%' : direccion_cliente.value,
            #item1
            '%ITEM1%' : item_name_1.value,
            '%QITEM1%' : quantity_item_1.value,
            '%PITEM1%' : price_item_1.value,
            #item2
            '%ITEM2%' : item_name_2.value,
            '%QITEM2%' : quantity_item_2.value,
            '%PITEM2%' : price_item_2.value,
            #item3
            '%ITEM3%' : item_name_3.value,
            '%QITEM3%' : quantity_item_3.value,
            '%PITEM3%' : price_item_3.value,
            #item4
            '%ITEM4%' : item_name_4.value,
            '%QITEM4%' : quantity_item_4.value,
            '%PITEM4%' : price_item_4.value,
            #item5
            '%ITEM5%' : item_name_5.value,
            '%QITEM5%' : quantity_item_5.value,
            '%PITEM5%' : price_item_5.value,
            #item6
            '%ITEM6%' : item_name_6.value,
            '%QITEM6%' : quantity_item_6.value,
            '%PITEM6%' : price_item_6.value,
            #item7
            '%ITEM7%' : item_name_7.value,
            '%QITEM7%' : quantity_item_7.value,
            '%PITEM7%' : price_item_7.value,
            #Total por items
            '%TITEM1%' : str(int(quantity_item_1.value) * int(price_item_1.value)),
            '%TITEM2%' : str(int(quantity_item_2.value) * int(price_item_2.value)),
            '%TITEM3%' : str(int(quantity_item_3.value) * int(price_item_3.value)),
            '%TITEM4%' : str(int(quantity_item_4.value) * int(price_item_4.value)),
            '%TITEM5%' : str(int(quantity_item_5.value) * int(price_item_5.value)),
            '%TITEM6%' : str(int(quantity_item_6.value) * int(price_item_6.value)),
            '%TITEM7%' : str(int(quantity_item_7.value) * int(price_item_7.value)),
            #Total
            '%TOTAL%' : str(
                            (int(quantity_item_1.value) * int(price_item_1.value))+
                            (int(quantity_item_2.value) * int(price_item_2.value))+
                            (int(quantity_item_3.value) * int(price_item_3.value))+
                            (int(quantity_item_4.value) * int(price_item_4.value))+
                            (int(quantity_item_5.value) * int(price_item_5.value))+
                            (int(quantity_item_6.value) * int(price_item_6.value))+
                            (int(quantity_item_7.value) * int(price_item_7.value))
                        )
                    }
        generar_factura(data_factura)
        if checbox.value:
            archivo = f"{nombre_cliente.value}_{fecha_facturacion.value}.docx"
            destinatario = correo_factura.value
            nombre_destinatario = nombre_cliente.value
            send_email(archivo,destinatario,nombre_destinatario)
            dialogo = ft.AlertDialog(title=ft.Text(f"Factura Generada, correo enviado a {correo_factura.value}"), 
                         on_dismiss=lambda e: print("Cerrado"))
        page.dialog = dialogo
        dialogo.open = True
        page.update()
    page.add(titulo, 
            ft.Row(controls=[fecha_facturacion]),
            ft.Row(controls=[nombre_cliente, direccion_cliente]),
            ft.Row(controls=[correo_factura, checbox]),
            # Items de la factura
            ft.Row(controls=[item_name_1, quantity_item_1, price_item_1]),
            ft.Row(controls=[item_name_2, quantity_item_2, price_item_2]),
            ft.Row(controls=[item_name_3, quantity_item_3, price_item_3]),
            ft.Row(controls=[item_name_4, quantity_item_4, price_item_4]),
            ft.Row(controls=[item_name_5, quantity_item_5, price_item_5]),
            ft.Row(controls=[item_name_6, quantity_item_6, price_item_6]),
            ft.Row(controls=[item_name_7, quantity_item_7, price_item_7]),
            ft.ElevatedButton('Generar Factura', on_click=obtener_datos)
            )

ft.app(target=main)