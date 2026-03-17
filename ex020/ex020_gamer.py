from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, real_name: str, nick: str):
        self.real_name = real_name
        self.nick = nick
        self.favorites = list()
    
    def add_favorite(self, game: str):
        self.favorites.append(game)
        self.favorites.sort()
    
    def gamer_record(self):
        record = Panel(f'Nome real: {self.real_name}\nJogos favoritos:')
        for g in self.favorites:
            record.renderable += '\n' + g
        print(record)

g1 = Gamer('Thiago Queiroz', 'kert_o.neihl')
g1.add_favorite('Minecraft')
g1.add_favorite('Genshin Impact')
g1.add_favorite('Albion Online')
g1.add_favorite('World of Warcraft')
g1.add_favorite('Forza Horizon')
g1.add_favorite('Counter Strike')
g1.gamer_record()
