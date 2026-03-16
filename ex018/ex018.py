from rich import print
from rich.panel import Panel

class Churrasco():
    def __init__(self, name: str, quant: int):
        self.name = name
        self.quant = quant

        self.consumption_per_person = 0.4
        self.meat_price = 82.40
    
    def analysis(self):
        quant_to_be_bought = self.consumption_per_person * self.quant
        total_cost = self.meat_price * quant_to_be_bought
        price_per_person = total_cost / self.quant

        Panel(f'''Analisando o [green]{self.name}[\] com [blue]{self.quant}[\] convidados:
        Cada participante comerá {self.consumption_per_person}kg e cada kg custa R${self.meat_price:.2f}.
        Recomendo comprar [blue]{quant_to_be_bought:.3f}kg[\] de carne.
        O custo total será de [green]R${total_cost:.2f}[\].
        Cada pessoa pagará [yellow]R${price_per_person:.2f}[\] para participar.''', title=self.name)
