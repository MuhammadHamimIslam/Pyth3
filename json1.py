import json

"parse json data to python dictionary"

# some json data
jsonData = '{"name": "python", "created": 1990}'

jsonObj = json.loads(jsonData) # parse json data to python dictionary 

print(f"dictionary is :{jsonObj}")
print(f"parsed name is: {jsonObj['name']}")

"parse python object to json data"

pyObj = {
    "name": "xyz",
    "age": 26,
    "profession": "programmer",
} # python object 


jsonObjData = json.dumps(pyObj) # parse python dictionary to json data
print(f"{jsonObjData = }")

# python object (list, tuple, boolean, None, str, int, float) can be converted to json
'-> json.dumps(obj, indent = 0, separators = (",", "="), sort_keys = True)'

print(json.dumps([1, 2, 3, 5]))

print(json.dumps({"name": "abc", "age": 29}, indent = 4, separators = (",", " = "), sort_keys = True))

"reading data from json file"

def readJsonFile(file): 
    with open(file) as f: # open the file
        content = f.read() # read the content
        jsonFileData = json.loads(content) # parse the json data to pyrhon object
    return jsonFileData

print(readJsonFile("test_data.json"))