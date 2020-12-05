# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 06:50:29 2020

@author: hungd
"""

#%% Read File

with open("input.txt") as file:
    array = file.read().strip()
array = [x for x in array.split("\n")]


#%% Question 1

maxID = 0
for i in range(len(array)):
    
    F = 0
    B = 127
    for j in range(len(array[i]) -3):   
        M = (B + F) // 2
        if array[i][j] == "F":
            B = M
        else:
            F = M + 1
            
    L = 0
    R = 7
    for j in range(len(array[i]) -3, len(array[i])):
        M = (R + L) // 2
        if array[i][j] == "L":
            R = M
        else:
            L = M + 1
            
    ID = F * 8 + L
    if ID > maxID:
        maxID = ID
    
#%% Question 2

IDs = []
for i in range(len(array)):
    
    F = 0
    B = 127
    for j in range(len(array[i]) -3):   
        M = (B + F) // 2
        if array[i][j] == "F":
            B = M
        else:
            F = M + 1
            
    L = 0
    R = 7
    for j in range(len(array[i]) -3, len(array[i])):
        M = (R + L) // 2
        if array[i][j] == "L":
            R = M
        else:
            L = M + 1
            
    ID = F * 8 + L
    IDs.append(ID)
    
IDs.sort()
for i in range(1, len(IDs)):
    if IDs[i] - 1 != IDs[i-1]:
        print(IDs[i] - 1)
        
            
            

        