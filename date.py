import datetime
import locale
import flet as ft

# Configurar el idioma para fechas en español
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")  # Asegúrate de que el locale esté instalado en tu sistema

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e):
        # Formatear la fecha en español
        fecha_en_espanol = e.control.value.strftime("%A, %d de %B de %Y").capitalize()
        page.add(ft.Text(f"Fecha seleccionada: {fecha_en_espanol}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"Selector de fecha cerrado"))

    page.add(
        ft.ElevatedButton(
            "Seleccionar fecha",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2023, month=10, day=1),
                    last_date=datetime.datetime(year=2024, month=10, day=1),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,
                )
            ),
        )
    )


ft.app(main)
