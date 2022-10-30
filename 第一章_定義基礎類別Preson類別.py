# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:43:23 2022

@author: 榮 鼎
"""
#定義基礎類別:Preson類別
class Preson():
    def __init__(self, name="", age=20, sex="man"):
        self.setname(name)
        self.setage(age)
        self.setsex(sex)
    def setname(self, name):
        if type(name)!=str:
            print("姓名必須是字串")
            return
        self.__name=name
    def setage(self, age):
        if type(age)!=int:
            print("年齡必須是整數")
            return
        self.__age=age
    def setsex(self, sex):
        if sex!="男" and sex!="女":
            print("性別輸入錯誤")
            return
        self.__sex=sex
    def show(self):
        print("姓名:", self.__name, "年齡:", self.__age ,"性別:", self.__sex)
        
class Studen(Preson):
    def __init__(self, name="", age=20, sex= "man", schoolyear=2016):
        super(Studen,self).__init__(name,age,sex)
        self.setschoolyear(schoolyear)
    def setschoolyear(self,schoolyear):
        self.schoolyear=schoolyear
    def show(self):
        Preson.show(self)
        print("入學時間:", self.schoolyear)        
    
    
if __name__ =='__main__':
    zhangsan=Preson("張三", 19, "男")
    zhangsan.show()
    lisi=Studen("李四", 18, "男", 2015)
    lisi.show()
    lisi.setage(20)
    lisi.show()
    
#P=1-36