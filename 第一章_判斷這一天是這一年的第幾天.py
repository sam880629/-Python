# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:21:46 2022

@author: 榮 鼎
"""
#判斷閏年
# year = int(input("輸入一個年份:"))

# if  year/4==0 and year/100 !=0 or  year / 400 == 0 :
#     print(year,"是閏年")
# else:
#     print(year,"不是閏年")    


#判斷這一天是這一年的第幾天
year = int(input("輸入年:"))
month = int(input("輸入月"))
day = int(input("輸入日"))
months =[0,31,59,90,120,151,181,212,243,273,304,334]

if 1<= month <=12 :
    sum = months[month-1]
else:
    print("月份錯誤")
sum += day
leap = 0
if  (year % 400 == 0) or((year%4==0) and (year%100 !=0))  :
    leap = 1
if(leap == 1) and (month>2):
    sum+=1
print("\n這一天是%d年的第%d天"% (year , sum))

#P1-18