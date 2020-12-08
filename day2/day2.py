# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:30:24 2020

@author: hungd
"""

f = open("day2input.txt")
array = [line for line in f.readlines()]
f.close

# O(n^2) time | O(1) space
def getNumOfCorrectCodes(array):
    
    numOfCorrectCodes = 0
    for i in range(len(array)):
        line = array[i]
        line = line.split(":")
        letter = line[0][-1]
        code = line[1].strip()
        
        minMax = line[0].split(" ")[0].split("-")
        min = int(minMax[0])
        max = int(minMax[1])
        
        count = 0
        for j in range(len(code)):
            if code[j] == letter:
                count += 1
                
        if min <= count <= max:
            numOfCorrectCodes += 1
        
    return numOfCorrectCodes

# O(n) time | O(1) space
def getNumOfCorrectCodes2(array):
    
    numOfCorrectCodes = 0
    for i in range(len(array)):
        line = array[i]
        line = line.split(":")
        letter = line[0][-1]
        code = line[1].strip()
        
        minMax = line[0].split(" ")[0].split("-")
        min = int(minMax[0]) - 1
        max = int(minMax[1]) - 1
        
        if code[min] == letter and code[max] != letter:
            numOfCorrectCodes += 1
        elif code[min] != letter and code[max] == letter:
            numOfCorrectCodes += 1
        
    return numOfCorrectCodes
    
    
getNumOfCorrectCodes(array)
getNumOfCorrectCodes2(array)