#!/usr/bin/python3

from gpiozero import *
from time import sleep
import automationhat

class Inventory:

    def __init__(self):

        self.run = True
        self.stretch_led = LED(19)
        self.water_led = LED(21)
        self.water_sensor = DigitalInputDevice(17)

    def manage(self):

        stretch_status = False
        water_status = False
        while self.run:

            value = automationhat.analog.one.read()
        #    print(value) 
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
    
            if self.water_sensor.value:
                self.water_led.on()
                if water_status == False:
                    water_status = True
                    print('Running Low on Water')
                    ## Notify Iotivity
            else:
                self.water_led.off()
                if water_status== True:
                    water_status = False
                    print('Plenty of Water')
                    ## Notify Iotivity 
    
            sleep(0.01)
            #sleep(1)


def main():
    x = Inventory()
    x.manage()


if __name__ == '__main__':
    main()
