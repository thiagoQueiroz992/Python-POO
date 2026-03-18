from rich import print
from rich.panel import Panel

class RemoteControl():
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.channels = [1, 2, 3, 4, 5]
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
        self.tv_panel.renderable = f'CHANNEL: {self.channel}\nVOLUME: {self.volume}'
        print(self.tv_panel)
        ipt = self.channel_and_volume()
        if ipt == '@':
            self.power_off()
        elif ipt == '<':
            self.previous_channel()
        elif ipt == '>':
            self.next_channel()
        elif ipt == '-':
            self.volume_down()
        elif ipt == '+':
            self.volume_up()
        elif ipt == '0':
            exit()
        else:
            self.power_on()

    def previous_channel(self):
        if self.channel == 1:
            self.channel = 5
        else:
            self.channel -= 1
        self.power_on()

    def next_channel(self):
        if self.channel == 5:
            self.channel = 1
        else:
            self.channel += 1
        self.power_on()

    def volume_down(self):
        if self.volume != 1:
            self.volume -= 1
        self.power_on()

    def volume_up(self):
        if self.volume != 5:
            self.volume += 1
        self.power_on()
    

rc = RemoteControl()
