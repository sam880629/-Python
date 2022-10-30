# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:38:58 2022

@author: 榮 鼎
"""
#列表產生式

L=[]
for i in range(1,10):
    L.append(i*i)
print(L,"\n")

#上面程式碼縮減成以下程式碼

print([x*x for x in range(1,10)],"\n")
   
#for循環後面加上if判斷

print([x*x for x in range(1,10) if x%2==0] )#偶數的平方才顯示
   
#P1-8