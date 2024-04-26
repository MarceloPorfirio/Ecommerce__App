import flet as ft
import pandas as pd
from io import StringIO

def main(page: ft.Page):
    # Controle para seleção de arquivo
    file_input = ft.FilePicker()
    upload_button = ft.FilledButton(text="Carregar")
    output_text = ft.TextField(multiline=True, expand=True)

    def on_file_uploaded(e):
        if e.control.files:
            file_info = e.control.files[0]
            if file_info.name.endswith('.csv'):
                # Lendo o arquivo CSV
                df = pd.read_csv(StringIO(file_info.get_bytes().decode('utf-8')))
                # Mostrando dados no TextField
                output_text.value = df.to_string()
                page.update()
            else:
                page.snack("Selecione um arquivo CSV.")

    file_input.on_change = on_file_uploaded
    page.add(file_input, upload_button, output_text)

ft.app(target=main)
