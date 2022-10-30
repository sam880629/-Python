# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:21:11 2022

@author: 榮 鼎
"""
#公有方法,私有方法,靜態方法的定義和呼叫
class Fruit:
    price=0
    def __init__(self):
        self.__color="Red"
        self.__city="Kunming"
    def __outputcolor(self):
        print(self.__color)
    def __outputcity(self):
        print(self.__city)
    def output(self):
        self.__outputcolor()
        self.__outputcity()
        
    def getPrice():
        return Fruit.price

    def setPrice(p):
        Fruit.price=p
        
        
apple=Fruit()
apple.output()
print(Fruit.getPrice())
Fruit.setPrice(9)
print(Fruit.getPrice())

#P1-34