#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

    def csipog(self):
        self.ev3.speaker.beep()
        
    def vonalkovet(self):
        #felvátva hajtom a motorokat egyik gyorsabb másik lassabb ha letér csere
        while True:
            if self.cs.reflection() > 35:
                self.bm.run(200)
                self.jm.run(100)
            else:
                self.jm.run(200)
                self.bm.run(100)
#ki íratjuk az akumlátor feszültségét és áramerősségét
    def aku(self): 
        volt =self.ev3.battery.voltage()/1000
        amper=self.ev3.battery.current()/1000
        print("A feszültség értéke: " + str(volt)+"V.")
        print("Az áramerrőség:" + str(amper)+"A.")
