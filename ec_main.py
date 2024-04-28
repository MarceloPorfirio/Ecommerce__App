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
       0:{
            "id": "111",
            "img_src:": "phone.jpg,",
            "nome": "Product 1",
            "description": "Ta procurando um Smartphone com alto desempenho, capaz de executar as tarefas mais comuns do dia a dia com velocidade e eficiência? Então vem conhcer o Moto G54 da Motorola. Para começar, esse smartphone faz parte da linha Moto G, tradicional linha de celulares da Motorola. Ele possui armazenamento interno de 256GB, espaço suficiente para guardar os arquivos como fotos e vídeos. Ah, sem falar que ele conta com tecnologia 5G, Processador Dimensity 7020 e Memória RAM de 8GB, dessa forma você tem uma boa performance em diversas atividades, das mais simples até algumas mais complexas. E esse modelo é na cor Azul. ",
            "price": "R$ 1200.00",
       },
       1:{
         "id": "112",
            "img_src:": "phone.jpg,",
            "nome": "Product 1",
            "description": "Ta procurando um Smartphone com alto desempenho, capaz de executar as tarefas mais comuns do dia a dia com velocidade e eficiência? Então vem conhcer o Moto G54 da Motorola. Para começar, esse smartphone faz parte da linha Moto G, tradicional linha de celulares da Motorola. Ele possui armazenamento interno de 256GB, espaço suficiente para guardar os arquivos como fotos e vídeos. Ah, sem falar que ele conta com tecnologia 5G, Processador Dimensity 7020 e Memória RAM de 8GB, dessa forma você tem uma boa performance em diversas atividades, das mais simples até algumas mais complexas. E esse modelo é na cor Azul. ",
            "price": "R$ 1300.00",  
       } ,
       2:{
           "id": "113",
            "img_src:": "phone.jpg,",
            "nome": "Product 1",
            "description": "Ta procurando um Smartphone com alto desempenho, capaz de executar as tarefas mais comuns do dia a dia com velocidade e eficiência? Então vem conhcer o Moto G54 da Motorola. Para começar, esse smartphone faz parte da linha Moto G, tradicional linha de celulares da Motorola. Ele possui armazenamento interno de 256GB, espaço suficiente para guardar os arquivos como fotos e vídeos. Ah, sem falar que ele conta com tecnologia 5G, Processador Dimensity 7020 e Memória RAM de 8GB, dessa forma você tem uma boa performance em diversas atividades, das mais simples até algumas mais complexas. E esse modelo é na cor Azul. ",
            "price": "R$ 1400.00",
       } ,
       3:{
           "id": "114",
            "img_src:": "phone.jpg,",
            "nome": "Product 1",
            "description": "Ta procurando um Smartphone com alto desempenho, capaz de executar as tarefas mais comuns do dia a dia com velocidade e eficiência? Então vem conhcer o Moto G54 da Motorola. Para começar, esse smartphone faz parte da linha Moto G, tradicional linha de celulares da Motorola. Ele possui armazenamento interno de 256GB, espaço suficiente para guardar os arquivos como fotos e vídeos. Ah, sem falar que ele conta com tecnologia 5G, Processador Dimensity 7020 e Memória RAM de 8GB, dessa forma você tem uma boa performance em diversas atividades, das mais simples até algumas mais complexas. E esse modelo é na cor Azul. ",
            "price": "R$ 1500.00",
       }
    }

    cart: dict = {}

    @staticmethod
    def get_products() -> dict:
        return Model.products
    
    @staticmethod
    def get_cart() -> dict:
        return Model.cart
    
class Product(ft.View):
    def _ini__(self, page: ft.Page) -> None:
        super(Product, self).__init__(route="/products")
        self.page = page

    def create_products(self, products: dict = Model.get_products()) -> None:

        for _, values in products.items():
            for key,value, in values.items():
                if key == "img_src":
                    ...
                if key == "name":
                    ...
                if key == "description":
                    ...
                if key == "id":
                    ...
                if key == "price":
                    ...
    
    def create_product_image(self, img_path: str):
        return ft.Container(image_src=img_path,image_fit="fill",
                            border_radius=6,padding=10)
    
    def create_product_text(self,name: str, description: str):
        return ft.Column([ft.Text(name, size=18), ft.Text(description,size=11)])
    
    def create_product_event(self, price: str, idd: str):
        return ft.Row(
            [
                ft.Text(price,size=14),
                ft.IconButton("add",data=idd,on_click=self.add_to_cart)
            ],
            alignment="spaceBetween"
        )

    


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