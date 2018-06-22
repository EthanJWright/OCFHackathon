#!/usr/bin/python3

from gpiozero import *
from time import sleep
import automationhat

class Stretch:

    def __init__(self):

        self.run = True
        self.stretch_led = LED(19)

    def manage(self):

        stretch_status = False
        while self.run:

            value = automationhat.analog.one.read()
            if value < 1.0:
                self.stretch_led.on()
                if stretch_status == False:
                    stretch_status = True
                    print('Running Low on Bananas')
                    ## Notify Iotivity
            else:
                self.stretch_led.off()
                if stretch_status == True:
                    stretch_status = False
                    print('Plenty of Bananas')
                    ## Notify Iotivity
    
            sleep(0.01)
            #sleep(1)


def main():
    x = Stretch()
    x.manage()


if __name__ == '__main__':
    main()
