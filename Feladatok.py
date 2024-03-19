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

        #időzitő
        self.ido=StopWatch()

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
        self.ev3.screen.print("A feszültség \nértéke: " + str(volt)+"V.")
        self.ev3.screen.print("Az áramerrőség: \n"+ str(amper)+"A.")
        wait(2000)

    def elsofeladat(self):
        #Mért értékek
        #fekete vonal:6
        #asztal lap:46 öszead osztva 2= 46+19/2=32.5
        #asztal széle felszin:19
        #asztaltól lefelé:0

        #reflection méri meg az  értéket
        ut=(46+19)/2
        while self.cs.reflection() >ut:
            self.robot.drive(100,0)
            print("visszaver fény:",self.cs.reflection(),".")
        self.robot.stop(Stop.BRAKE)
    
    def masodikfeladat(self):
        #ujra inditotom a stoppert
        self.ido.reset() 
        ut=(46+19)/2
        while self.cs.reflection() >ut:
            self.robot.drive(100,0)
            #print("visszaver fény:",self.cs.reflection(),".")
        self.robot.stop(Stop.BRAKE)
        eleteltIdo=self.ido.time()
        #aktuális érték visszaadás
        self.robot.drive(-100,0) #hátra
        wait(eleteltIdo)
        self.robot.stop(Stop.BRAKE)