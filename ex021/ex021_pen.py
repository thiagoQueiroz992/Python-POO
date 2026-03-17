from rich import print

class Pen():
    def __init__(self, color: str):
        self.color = color
        self.uncovered = False