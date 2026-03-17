from rich import print
from rich.panel import Panel

class RemoteControl():
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.is_tv_on = False
        self.tv_panel = Panel('TV')
        print('Hello World')
    

rc = RemoteControl()
