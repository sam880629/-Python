# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:08:47 2022

@author: 榮 鼎
"""
#定義含有實例屬性

class Person:

    def __init__(self, str,n):
        self.name=str
        self.age=n
    def SayHello(self):
        print("Hello")
    def Printname(self):
        print("姓名:", self.name ,"年齡:",self.age)
    def PrintNum(self):
        print(Person.num)
        
P1=(Person("夏敏捷",42))
P2=(Person("王琳",36))
P1.Printname()
P2.Printname()
Person.num=2
P1.PrintNum()
P2.PrintNum()

#P1-32        