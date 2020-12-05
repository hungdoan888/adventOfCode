# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:41:40 2020

@author: hungd
"""

f = open("input.txt", "r")
array = f.readlines()
f.close

for i in range(len(array)):
    array[i] = array[i][:-1]

# Repeat string enough times to go down the whole time
# O(nlog(m)) time
def numTreeEncountered(array, VposPlus, HposPlus):
    
    for i in range(len(array)):
        while len(array[i]) < len(array) * (HposPlus + 20):
            array[i] = array[i] + array[i]
            
    for i in range(len(array)):
        array[i] = list(array[i])
     
    Hpos = 0
    Vpos = 0
    count = 0
    
    while Vpos <= len(array) - 1:
        if array[Vpos][Hpos] == "#":
            array[Vpos][Hpos] = "X"
            count += 1
        else:
            array[Vpos][Hpos] = "O"
            
        Vpos += VposPlus
        Hpos += HposPlus
        
    return count
        
# Part 2
def getAllTreeHit(array):
    HposPlus = [1, 3, 5, 7, 1]
    VposPlus = [1, 1, 1, 1, 2]
    
    multipliedTogether = 1
    for i in range(len(HposPlus)):
        count = numTreeEncountered(array, VposPlus[i], HposPlus[i])
        multipliedTogether *= count 
        print(count)
        
    return multipliedTogether

getAllTreeHit(array)