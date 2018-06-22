#!/usr/bin/python3

from gpiozero import *
from time import sleep
import automationhat
from SocketWriter import * 

class Stretch:

    def __init__(self):

        self.run = True
        self.stretch_led = LED(19)
        self.writer = SocketWriter("/var/iotivity/toOCFStretch")

    def manage(self):

        old_value = -1
        stretch_status = False
        while self.run:

            value = automationhat.analog.one.read()
          
            if old_value != value:
                print('Changed Value')
                self.writer.sendNewDeviceResponse(value, "number", "gpio")
            
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
   
            old_value = value
            sleep(0.2)
            #sleep(1)


def main():
    x = Stretch()
    x.manage()


if __name__ == '__main__':
    main()
