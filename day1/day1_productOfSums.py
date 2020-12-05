# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:59:57 2020

@author: hungd
"""

f = open("input.txt", "r")
array = [int(line) for line in f.readlines()]
f.close

# O(nlog(n)) time | O(1) space
def findProductofSumof2020(array):
    array.sort()
    left = 0
    right = len(array) - 1
    
    while left < right:
        if array[left] + array[right] == 2020:
            return array[left] * array[right]
        elif array[left] + array[right] < 2020:
            left += 1
        else:
            right -= 1
            
            
findProductofSumof2020(array)


# O(n^2) time | O(1) space
def findProductofThreeSumsof2020(array):
    array.sort()
    
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        
        while left < right:
            if array[i] + array[left] + array[right] == 2020:
                return array[i] * array[left] * array[right]
            elif array[i] + array[left] + array[right] < 2020:
                left += 1
            else:
                right -= 1
            
            
findProductofThreeSumsof2020(array)

