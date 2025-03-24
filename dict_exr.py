"A function to convert a list of tuples to dictionary"

def convToDict(inpList):
  result = {} # result holder 
  for i in inpList: #loop through the list
      # append the first as key and 2nd as value
      result[i[0]] = i[1] 
  return result

"A function to merge multiple dictionaries to one"

def merge(*dictionaries):
    result = dictionaries[0] # result is set to the 1st element 
    for i in dictionaries: # loop the dicts
        result.update(i) # now update result 
    return result

"A function to count the frequency of each character in a string"

def wordFrequency(st): 
  # initial dictionary 
  result = {}
  for char in st.lower(): # loop inside the string -> case insensitive 
    if char not in result: result[char] = 1
    else: result[char] += 1
  return result

"A function to group words by their lengths"

def groupByLength(fruits): 
    result = {} # result holder 
    for fruit in fruits: # loop the fruits 
        length = len(fruit) #get the length 
        if length not in result: 
            # if result isn't in result create one
            result[length] = []
        # append fruit in the result ,
        result[length].append(fruit)
    return result 

"A function to invert a dictionary"        
    
def invertDict(dictionary): 
    result = {} # result holder 
    for key, value in dictionary.items(): # loop the dictionary 
        if value not in result: # if value not in result then initialize it
            result[value] = []
        result[value].append(key)
    for elm in result: 
        # if item's length is one then make it string 
        if len(result[elm]) == 1: 
            result[elm] = result[elm][0]
    return result

"A function to handle missing key in a dictionary"

def handleMissing(dictionary, key): 
    if key in dictionary: 
        return f"{key}: {dictionary[key]}"
    else:
        return "key not found"

"A function to create dictionary from matrix"

def matrixToDict1(matrix):
    result = {} # result holder 
    for elm in matrix: 
        # append result at the index of the element+1 amd value is the elm
        result[matrix.index(elm) + 1] = elm
    return result 
def matrixToDict2(matrix):
    # dict compression: result will be append for the key of x+1 and the value will be the item in the matrix 
    return {x+1: matrix[x] for x in range(len(matrix))}

"A function to create a nested dictionary with the key of given input list"

def nestedDict(inpDict, inpList): 
    result = {}
    # loop the input list 
    for i in range(len(inpList)):
        key, value = list(inpDict.items())[i]
        result[inpList[i]] = {key: value}
    return result 
       
"A function to filter and sort a list of users dictionary by their age"

def filterByAge(users): 
    result = []
    for user in users: # loop the users 
    # if user's age is more than 18 then append the user to result 
        if user["age"] >= 18: 
            result.append(user)
    # now sort by their age
    result.sort(key = lambda a: a["age"])
    return result 

"A function to remove keys with same values in a dictionary"

def removeSameValues(inpDict): 
    result = {} # result holder 
    dictValue = list(inpDict.values()) # a list of dictionary's value 
    unique = [elm for elm in dictValue if dictValue.count(elm) == 1] # find the unique 
    for key, value in inpDict.items(): 
    # loop the dictionary, if value is found in unique list then append to the result 
        if value in unique: 
            result[key] = value
    return result 

"A function to extract dictionary with each key having non-numeric value from a given dictionary"

def extractNonNumeric(inpDict): 
    result = {} # result holder 
    for key, value in inpDict.items():
    # loop the dictionary, if value is non-numeric then append it to the result 
        if not isinstance(value, (int, float)):
            result[key] = value
    return result

"A function to calculate the toal price of the items of input dictionary's list"

def totalPrice(inpList): 
    total = 0 # result holder 
    for item in inpList: 
        total += item["quantity"] * item["price"]
        print(item)
    return total

"A function to calculate the toal price of the items of input dictionary's list. N.B-> 10% discount will be applied to every 3 items"

def totalPriceWithDiscount(inpList): 
    result = 0 # result holder 
    payRate = 0.9 # when 10% discount 
    for item in inpList:
        # discountable item
        discountable = (item["quantity"] // 3) * 3
        # non discountable item
        nonDiscountable = (item["quantity"] % 3)
        # calculate the price of the discountable items 
        priceWithDiscount = discountable * item["price"] * payRate
        # calculate the price of the non-discountable items 
        priceWithoutDiscount = nonDiscountable * item["price"]
        # now update the result with the sum of both non-discountable and discountable 
        result += (priceWithDiscount + priceWithoutDiscount)
    return result 


