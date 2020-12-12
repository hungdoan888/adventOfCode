# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:18:30 2020

@author: hungd
"""

#%% Read File

with open("input.txt") as file:
    array = file.read().strip()
array = [x for x in array.split("\n")]

#%% Finding Bags

bags = {}
for i in range(len(array)):
    line = array[i]
    line = line.split("contain")
    
    
    parentBag = line[0].strip()
    bags[parentBag] = []
    
    childBags = line[1]
    if "no other" in childBags:
        bags[parentBag] = None
        continue
    
    childBags = childBags.replace("bags", "")
    childBags = childBags.replace("bag", "")
    childBags = childBags.strip(".")
    childBags = childBags.split(",")

    for j in range(len(childBags)):
        childBag = childBags[j].strip()
        index = childBag.find(" ")
        childBagNum = int(childBag[:index])
        childBag = childBag[index+1:]
        
        bags[parentBag].append({childBag: childBagNum})

# Finding number of out bags contiaining gold bags
keyWord = "shiny star"
keyWords = {}

def getGoldStar(bags, keyWord):
    for i in range(len(bags)):
        parent = list(bags.keys())[i] 
        
        if bags[parent] is None:
            continue
        
        for j in range(len(bags[parent])):
            if keyWord in bags[parent][j]:
                count += 1
            
    
    
    
    
    
    
    
    
    
    
    
        