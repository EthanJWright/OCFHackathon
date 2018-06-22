#!/usr/bin/env python

import time

import automationhat
time.sleep(0.1) # short pause after ads1015 class creation recommended

class Sensor():
    def __init__(self):
        self.one = 0.0
        self.two = 0.0
        self.three = 0.0
        self.continiue = True


    def start_monitor(self):
        while(self.continiue):
            new_one = automationhat.analog.one.read()
            new_two = automationhat.analog.two.read()
            new_three = automationhat.analog.three.read()
            if ( self.one != new_one  or self.two != new_two or self.three != new_three ):
                self.one = new_one
                self.two = new_two
                self.three = new_three
                print("Total = " + str( new_one + new_two + new_three))
            time.sleep(0.25)

s = Sensor()
s.start_monitor()
