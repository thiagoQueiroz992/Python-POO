from rich import print

class Employee():
    def __init__(self, name: str, sector: str, position: str):
        self.name = name
        self.sector = sector
        self.position = position
        
        self.company = 'Curso em Vídeo'
    
    def presenting(self):
        return f':handshake: Olá, sou [blue]{self.name}[/] e sou {self.position} no setor de {self.sector} da empresa {self.company}.'
