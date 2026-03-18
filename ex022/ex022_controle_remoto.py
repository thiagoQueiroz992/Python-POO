from rich import print
from rich.panel import Panel

class RemoteControl():
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.tv_panel = Panel('sacrifice your hearts', title='[ TV ]', width=40)
        self.input = ''
        self.power_off()
    
    def channel_and_volume(self):
        self.input = str(input('< CH >   < VOL > ::  '))
        return self.input

    def power_off(self):
        self.tv_panel.renderable = 'TV is off'
        print(self.tv_panel)
        if self.channel_and_volume() == '@':
            self.power_on()
    
    def power_on(self):
        self.tv_panel.renderable = 'CHANNEL\nVOLUME'
        print(self.tv_panel)
        if self.channel_and_volume() == '@':
            self.power_off()
    

rc = RemoteControl()
