myDict = {
  "name": "xyz",
  "age": 27,
  "isProgrammer": True,
  "learned Language": ["JavaScript", "C", "Python", "Html", "Css"],
  "codingJourney": "From 2023"
}

print("The dictionary is: ", myDict)

"accessing item in dictionary"

print(f"Name is :{myDict['name']}") # prints the name 

print(f"Name is: {myDict.get("name", "unknown")}") # prints the name. It also takes a default value in the 2nd parameter 

"loop through a dictionary"

for i in myDict: 
  print(f"{i}: {myDict[i]}")
  
