#!/usr/bin/python3

from gpiozero import *
from time import sleep
import automationhat
from SocketWriter import *

class Water:

    def __init__(self):

        self.run = True
        self.water_led = LED(21)
        self.water_sensor = DigitalInputDevice(17)
        self.writer = SocketWriter("/var/iotivity/toOCFWater")

    def manage(self):

        water_status = False
        while self.run:

            if self.water_sensor.value:
                self.water_led.on()
                if water_status == False:
                    water_status = True
                    print('Running Low on Water')
                    self.writer.sendNewDeviceResponse(True, "boolean", "gpio") ## Notify Iotivity
            else:
                self.water_led.off()
                if water_status== True:
                    water_status = False
                    print('Plenty of Water')
                    self.writer.sendNewDeviceResponse(False, "boolean", "gpio") ## Notify Iotivity 
    
            sleep(0.2)
            #sleep(1)


def main():
    x = Water()
    x.manage()


if __name__ == '__main__':
    main()
