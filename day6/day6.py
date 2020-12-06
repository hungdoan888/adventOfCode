# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:12:58 2020

@author: hungd
"""

#%% Read File

with open("input.txt") as file:
    array = file.read().strip()
array = [x for x in array.split("\n")]
array.append("")

#%% Questions 1

total_count = 0
groupDict = {}
for i in range(len(array)):
    
    if array[i] == "":
        total_count += len(groupDict)
        groupDict = {}
        
    for j in range(len(array[i])):
        if array[i][j] not in groupDict:
            groupDict[array[i][j]] = True
print(total_count)
        
#%% Question 2

group_count = 0
total_count = 0
for i in range(len(array)):
    
    if array[i] == "":
        count = 0
        dict_values = list(groupDict.values())
        for j in range(len(dict_values)):
            if dict_values[j] == group_count:
                count += 1  
        total_count = total_count + count
        
        groupDict = {}
        group_count = 0
        
        continue
        
    for j in range(len(array[i])):
        if array[i][j] in groupDict:
            groupDict[array[i][j]] += 1
        else:
            groupDict[array[i][j]] = 1
        
    group_count += 1
    
print(total_count)