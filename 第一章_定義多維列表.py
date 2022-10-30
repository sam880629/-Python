# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:58:59 2022

@author: Sam
"""
#定義3行6列的二維清單，列印出元素值

rows = 3 
cols = 6
martix = [[ 0 for col in range(cols)] for row in range(rows)]

#列表產生式產生二維列表
# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for i in range(rows):
    for j in range(cols):
        martix[i][j] = i * 3 + j
        print(martix[i][j],end=",")
    print("\n")
    
#P1-7