myDict = {
  "name": "xyz",
  "age": 27,
  "isProgrammer": True,
  "learnedLanguage": ["JavaScript", "C", "Python", "Html", "Css"],
  "codingJourney": "From 2023"
}

print("The dictionary is: ", myDict)

"accessing item in dictionary"

print(f"Name is :{myDict['name']}") # prints the name 

print(f"Name is: {myDict.get("name", "unknown")}") # prints the name. It also takes a default value in the 2nd parameter 

dictKey = myDict.keys() # gets the keys of the dictionary 
print(dictKey)

dictValue = myDict.values() # gets the values of the dictionary 
print(dictValue)

dictItm = myDict.items() # makes a tuple of the values of the dictionary 
print(dictItm)

"loop through a dictionary"

for i in myDict: 
  print(f"{i}: {myDict[i]}") # prints the dictionary 

for i in myDict.values(): 
  print(f"the value is: {i}") # prints the values of the dict
for i in myDict.keys(): 
  print(f"the key is: {i}") # prints the keys of the dict
for key, value in myDict.items(): 
  print(f"value in '{key}' is: {value}") # prints the value and keys of the dict
  
"Updating a dictionary"

myDict["age"] = 28 # update the age to 28
print("The dictionary is: ", myDict)

myDict.update({"age": 29}) # update the age to 29
print("The dictionary is: ", myDict)

myDict["favorite Language"] = "JavaScript" # adds a new item
print("The dictionary is: ", myDict)

"copying a dictionary"

newDict1 = myDict.copy()
print("The new dictionary is: ", newDict1)

newDict2 = dict(myDict)
print("The new dictionary is: ", newDict2)

"removing item from dictionary"

myDict.pop("codingJourney") # removes the item
print("The dictionary is: ", myDict)

myDict.popitem() # removes the last added item
print("The dictionary is: ", myDict)

del myDict["isProgrammer"] # deletes the item
print("The dictionary is: ", myDict)

myDict.clear() # clears the full list
print("The dictionary is: ", myDict)
