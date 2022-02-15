#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Main.py
#  
#  Copyright 2022  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  To get GPIO working
#    sudo apt update
#    sudo apt upgrade
#    sudo apt install rpi.gpio
#
#	sudo raspi-config
#     > Interface updates
#        > Enable I2C and SPI in raspi-config

class LogicGate:
    def __init__(self):
        self.led = LED(25)
        #self.gpio25 = GPIO(25)
    
    def turnOnLED(self):
        print("turning ON LED")
        self.led.on()
        
    def turnOffLED(self):
        print("turning OFF LED")
        self.led.off()

    def diagnosis(self):
        while True:        
            action = raw_input("turn on led? (y/n)").upper()                
            if action not in "YNX" or len(action) != 1:
                print("I don't know how to do that")
                continue            
            if action == "Y":
                self.turnOnLED()
            elif action == "N":
                self.turnOffLED()
            elif action == "X":
                break

if __name__ == '__main__':
    import sys
    from time import sleep
    from gpiozero import LED
    from gpiozero import Button
        
    button = Button(2)
    gate = LogicGate()
    print("Logic Gate Started")
    
    #gate.diagnosis()
    while True:
        if button.is_pressed:
            gate.turnOnLED()
            sleep(10)
            gate.turnOffLED();
        
        
            
        
            
