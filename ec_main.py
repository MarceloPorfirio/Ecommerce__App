import flet as ft

class Landing(ft.View):
    def __init__(self,page: ft.Page) -> None:
        super(Landing,self).__init__(
            
        )

def main(page:ft.Page) -> None:
    page.add(ft.SafeArea(ft.Text("Hello, Flet")))

ft.app(main)