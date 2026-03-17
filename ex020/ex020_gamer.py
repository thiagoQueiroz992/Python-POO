from rich import print
from rich.panel import panel

class Gamer():
    def __init__(self, real_name: str, nick: str):
        self.real_name = real_name
        self.nick = nick