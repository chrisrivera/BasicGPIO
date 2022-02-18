#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LogicGate.py
#  
#  Copyright 2022  <chrisrivera>
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


class LogicGate:
    def __init__(self):
        self._switch_1 = 0          #Not initialized        
        self._switch_2 = 0          #Not initialized    
        self._switch_3 = 0          #Not initialized    
        GPIO.setmode(GPIO.BCM)        
        self.led = LED(25)          #LED        
        GPIO.setup(4,GPIO.IN)       #Switch1 UP
        GPIO.setup(17,GPIO.IN)      #Switch1 DOWN
        GPIO.setup(18,GPIO.IN)      #Switch2 UP
        GPIO.setup(23,GPIO.IN)      #Switch2 DOWN        
        GPIO.setup(16,GPIO.IN)      #Switch3 UP
        GPIO.setup(21,GPIO.IN)      #Switch3 DOWN
        
    @property
    def switch_1(self):
        return self._switch_1
    
    @property
    def switch_2(self):
        return self._switch_2
    
    @property
    def switch_3(self):
        return self._switch_3
                
    def refreshState(self):        
        if GPIO.input(4):
            self.switch_1 = -1           #if 17 is grounded (SWITCH DOWN)
        elif GPIO.input(17):
            self.switch_1 = 1            #if 4 is grounded (SWITCH UP)
        if GPIO.input(18):
            self.switch_2 = -1           #if 23 is grounded (SWITCH DOWN)
        elif GPIO.input(23):
            self.switch_2 = 1            #if 17 is grounded (SWITCH UP)
        if GPIO.input(16):
            self.switch_3 = -1           #if 21 is grounded (SWITCH DOWN)
        elif GPIO.input(21):
            self.switch_3 = 1            #if 16 is grounded (SWITCH UP)
        
    
    
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

       
def switchDiagnostic(switchState):
    if switchState[0] == 1:        
        print("SW 1 - UP")
    if switchState[0] == -1:        
        print("SW 1 - DOWN")
    if switchState[1] == 1:       
        print("SW 2 - UP")
    if switchState[1] == -1:        
        print("SW 2 - DOWN")
    if switchState[2] == 1:
        print("SW 3 - UP")
    if switchState[2] == -1:
        print("SW 3 - DOWN")

def getState(gate, switchState):
    if gate.switch_1 == 1 and switchState[0] != gate.switch_1:
        switchState[0] = gate.switch_1
    if gate.switch_1 == -1 and switchState[0] != gate.switch_1:
        switchState[0] = gate.switch_1        
    if gate.switch_2 == 1 and switchState[1] != gate.switch_2:
        switchState[1] = gate.switch_2
    if gate.switch_2 == -1 and switchState[1] != gate.switch_2:
        switchState[1] = gate.switch_2
    if gate.switch_3 == 1 and switchState[2] != gate.switch_3:
        switchState[2] = gate.switch_3
    if gate.switch_3 == -1 and switchState[2] != gate.switch_3:
        switchState[2] = gate.switch_3        
            
if __name__ == '__main__':
    import sys
    import array
    import RPi.GPIO as GPIO
    
    from time import sleep
    from gpiozero import LED
    from gpiozero import Button
    
    gate = LogicGate()
    print("Logic Gate Started")
    switchState = [0] * 3           #array of length 3
    
    #gate.diagnosis()       
    button = Button(2)              #SDA    (ACTION)
        
    while True:
        sleep(0.001)                #restrict clocks        
        gate.refreshState()        
        getState(gate, switchState)
        
        #switchDiagnostic(switchState)
                
        if button.is_pressed:
            print('switch state:',switchState[0],switchState[1],switchState[2])            
            if switchState[0] == 1 and switchState[1] == 1 and switchState[2] == 1:
                print("all green, turning light on!")
                gate.turnOnLED()
            else:
                gate.turnOffLED()
            sleep(1)                #dont over press button

            
        
