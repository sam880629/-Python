# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:08:48 2022

@author: 榮 鼎
"""
#為Car類別定義私有成員
class car:
  
    def __init__(self, c, w):
        self.color=c
        self.__weight=w
        
car1=car("Red",1.8)
car2=car("Blue",2)
print(car1.color)
print(car1._car__weight) 

#P1-33