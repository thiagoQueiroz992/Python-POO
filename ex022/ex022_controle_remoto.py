from rich import print
from rich.panel import Panel
from os import system
from time import sleep

class RemoteControl():
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.tv_panel = Panel('sacrifice your hearts', title='[ TV ]', width=50)
        self.input = ''
        self.power_off()
    
    def channel_and_volume(self):
        self.input = str(input(f'< CH{self.channel} >   - VOL{self.volume} + ::  '))
        return self.input

    def power_off(self):
        system('cls')
        self.tv_panel.renderable = ':prohibited: [red bold]TV is off. Type @ to power it on.[/]'
        print(self.tv_panel)
        ipt = self.channel_and_volume()
        if ipt == '@':
            print(':warning: [yellow bold]Turning TV on...[/]')
            sleep(2)
            self.power_on()
        elif ipt == '0':
            exit()
        else:
            self.power_off()
    
    def power_on(self):
        system('cls')
        volume_control = '[on white][on green]' + ' ' * self.volume + '[/on green]' + ' ' * (5 - self.volume) + '[/]'
        self.tv_panel.renderable = f'[blue bold]CHANNEL[/] =  1  2  3  4  5 \n[blue bold]VOLUME[/]  = {volume_control}'.replace(f' {self.channel} ', f'[bold on yellow] {self.channel} [/]')
        print(self.tv_panel)
        ipt = self.channel_and_volume()
        if ipt == '@':
            print(':warning: [yellow bold]Turning TV off...[/]')
            sleep(2)
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
