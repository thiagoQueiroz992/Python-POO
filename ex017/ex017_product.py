from rich import print
from rich.panel import Panel
from rich.align import Align

class Product():
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def label(self):
        product_label = Panel(Align(self.name.center(50) + '\n' + '-' * 50 + '\n' + f'R${self.price:,.2f}'.center(50), 'center'), title='Product')
        print(product_label)

p1 = Product('iPhone 17 Pro Max', 23_000)
p2 = Product('Mangá Vinland Saga', 45)
p3 = Product('Monitor Gamer 240hz FHD', 1_200)
p1.label()
p2.label()
p3.label()
