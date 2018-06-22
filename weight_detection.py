#!/usr/bin/env python

import time
from SockerWriter import *
import automationhat

time.sleep(0.1) # short pause after ads1015 class creation recommended

class WeightSensor():
    def __init__(self):
        # Loop
        self.cont = True
       
        # Vals
        self.one = 0.0
        self.two = 0.0
        self.three = 0.0

        self.sum = 0.0
       
        self.writer = SockerWriter("/tmp/socket/toOCFWeight")


    def start_monitor(self):

        while(self.cont):
            self.one = automationhat.analog.one.read()
            self.two = automationhat.analog.two.read()
            self.three = automationhat.analog.three.read()

            newSum = new_one + new_two + new_three

            if ( newSum != self.sum):
                self.sendNewDeviceResponse
                self.writer.sendNewDeviceResponse(newSum, "number", "gpio")
                self.sum = newSum

            time.sleep(0.20)

if __name__ == "__main__":
    s = Sensor()
    s.start_monitor()
