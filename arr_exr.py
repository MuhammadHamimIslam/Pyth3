import array as arr


"A function to find out the maximum number in an array"
def findMax(inpArr):
    result = inpArr[0] # set max number to the first element 
    for i in inpArr: 
        # if other element is greater than result then result = this
        if i > result: 
            result = i
    return result 

"A function to filter all odd numbers in an array"

def filterOdd(inpArr): 
    result = arr.array("i") # result holder 
    for i in inpArr: 
        if i % 2 == 0: # if item is even append it to result 
            result.append(i)
    return result 

"A function to find the average of given input array"

def avg(inpArr): 
    return sum(inpArr) / len(inpArr)

"A function to find difference between each number"

def findDeference(inpArr): 
    result = arr.array("i") # result holder 
    for i in range(len(inpArr) - 1): 
        # now append the deference to the array.
        result.append(inpArr[i + 1] - inpArr[i]) 
    return result 

"A function to split an array in two and store even numbers in one array and odd numbers in the other"

def splitArray(inpArr):
    odds = [] # odd numbers holder 
    evens = [] # even numbers holder 
    for i in inpArr: 
        if i % 2 == 0: 
            evens.append(i) # append even numbers 
        else:
            odds.append(i) # append odd numbers 
    return [evens, odds]

"A function to perform insertion sort on an array"