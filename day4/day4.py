# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 07:42:57 2020

@author: hungd
"""

f = open("input.txt", "r")
array = f.readlines()
f.close

# Create an extra "\n" at the end to get the last set of data
array.append("\n")

# Problem 1
def problem1(array):
    data = {}
    data["passports"] = []
    temp_dict = {}
    
    # Put in Dictionary
    for i in range(len(array)):
        
        if array[i] == "\n":
            data["passports"].append(temp_dict)
            temp_dict = {}
        
        # Format line
        array[i] = array[i].strip("\n").split()
        
        for j in range(len(array[i])):
            array[i][j] = array[i][j].split(":")
            
            # Add to temp dict
            temp_dict[array[i][j][0]] = array[i][j][1]
        
    # Check if attributes are in dictionary
    attributes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 
    validPassports = []
    for i in range(len(data["passports"])):
        count = 0
        for j in range(len(attributes)):
            if attributes[j] in data["passports"][i]:
                count += 1
                
        if count == 7:
            validPassports.append(1)
        else:
            validPassports.append(0)
            
    return validPassports, data

validPassports, data = problem1(array)
print("Problem 1:", sum(validPassports))

# Problem 2
data["validPassportsfrom1"] = []
for i in range(len(validPassports)):
    if validPassports[i] == 1:
        data["validPassportsfrom1"].append(data["passports"][i])

count = 0
for i in range(len(data["validPassportsfrom1"])):
    
    # Birth Year
    if len(data["validPassportsfrom1"][i]["byr"]) != 4 or \
       int(data["validPassportsfrom1"][i]["byr"]) < 1920 or \
       int(data["validPassportsfrom1"][i]["byr"]) > 2002:
        continue
    
    # Issue Year
    if len(data["validPassportsfrom1"][i]["iyr"]) != 4 or \
       int(data["validPassportsfrom1"][i]["iyr"]) < 2010 or \
       int(data["validPassportsfrom1"][i]["iyr"]) > 2020:
        continue
    
    # Expiration Year
    if len(data["validPassportsfrom1"][i]["eyr"]) != 4 or \
       int(data["validPassportsfrom1"][i]["eyr"]) < 2020 or \
       int(data["validPassportsfrom1"][i]["eyr"]) > 2030:
        continue
    
    # Height
    if len(data["validPassportsfrom1"][i]["hgt"]) < 3:
        continue
    
    number = data["validPassportsfrom1"][i]["hgt"][:-2]
    units = data["validPassportsfrom1"][i]["hgt"][-2:]
    
    try:
        number = int(number)
    except:
        continue
    
    if units == "cm" or units == "in":
        pass
    else:
        continue
    
    if units == "cm":
        if number < 150 or number > 193:
            continue
    elif units == "in":
        if number < 59 or number > 76:
            continue
        
    # Hair Color
    hcl = data["validPassportsfrom1"][i]["hcl"]
    if len(hcl) != 7:
        continue
    
    if hcl[0] != "#":
        continue
    
    allowableCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                           "a", "b", "c", "d", "e", "f"]
    
    cont = False
    for j in range(1, len(hcl)):
        if hcl[j] not in allowableCharacters:
            cont = True
            break
    if cont:
        continue
    
    # Eye Color
    ecl = data["validPassportsfrom1"][i]["ecl"]
    allowableEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl not in allowableEyeColors:
        continue
    
    # Passport ID
    pid = data["validPassportsfrom1"][i]["pid"]
    
    if len(pid) != 9:
        continue
    
    try:
        int(pid)
    except:
        continue
    
    count += 1
    
print(count)
    
























