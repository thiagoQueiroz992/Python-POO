from rich import print

class Pen():
    def __init__(self, color: str):
        self.color = color
        self.uncovered = False
    
    def uncover(self):
        self.uncovered = True

    def cover(self):
        self.uncovered = False
    
    def write(self, text: str):
        if self.uncovered:
            print(f'[{self.color}]' + text + '[/]', end=' ')
        else:
            print(':prohibited: A caneta está [yellow]tampada[/]! Destampe-a para poder escrever.')
    
    def break_line(self, lines = 1):
        print('\n' * lines)


p1 = Pen('red')
p2 = Pen('blue')
p3 = Pen('yellow')

p1.write('Hello World!')

p1.uncover()
p2.uncover()
p3.uncover()

p1.write('Hello World!')
p1.break_line()
p2.write('How it\'s going?')
p2.break_line(1)
p3.write('Bye')
p3.break_line(3)

p3.cover()
p3.write('Bye bye')
