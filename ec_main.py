import flet as ft

class Landing(ft.View):
    def __init__(self,page: ft.Page) -> None:
        super(Landing,self).__init__(
            route="/", horizontal_alignment="center",
            vertical_alignment="center"
        )

        self.page = page
        self.cart_logo = ft.Icon(name=ft.icons.SHOPPING_CART_OUTLINED,size=64)
        self.title = ft.Text("Simple Store".upper(),size=28)
        self.subtitle = ft.Text("Desenvolvido com Flet",size=11)

        self.produtct_page = ft.IconButton("arrow_forward",
                                           width=54,
                                           height=54,
                                           style=ft.ButtonStyle(
                                               bgcolor={"":"#202020"},
                                               shape={"":ft.RoundedRectangleBorder(radius=8)},
                                               side={"":ft.BorderSide(2,"white54")}
                                           ),
                                           on_click=lambda e: self.page.go("/products")
                                           )


        self.controls = [
            self.cart_logo,
            ft.Divider(height=25,color="transparent"),
            self.title,
            self.subtitle,
            ft.Divider(height=10,color="transparent"),
            self.produtct_page
        ]

class Model(object):
    products: dict ={
        
    }
class Product(ft.View):
    def _ini__(self,) -> None:
        super(Product, self).__init__(route="/products")
        


def main(page:ft.Page) -> None:
    def router(route) -> None:
        page.views.clear()

        if page.route == "/":
            landing = Landing(page)
            page.views.append(landing)
        
        if page.route == "/products":
            products = Product(page)
            page.views.append(products)

        page.update()
    page.on_route_change = router
    page.go("/")

ft.app(main)