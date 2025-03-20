import array as arr

"As array isn't a built in data type in python.We need to import the 'array' module"
"""
array syntax:
    Array = arr.array("typecode", values)
    
'typecode' is used to define the data type of the array 

typecode --------------> data type 
'b', 'h', 'i', 'l', 'q'  signed int
'B', 'H', 'I', 'L', 'Q'  unsigned int
'u'                      unicode char
'f', 'd'                 floating num

and value can be list, tuple, dictionary 
"""
# an array with int type
intArr = arr.array("b", [1, 2, 3, 4, 5])
print(f"integer type array: {intArr}\n type: {type(intArr)}\n")

# an array with char type 
charArr = arr.array("u", "Hello, World!")
print(f"character type array: {charArr}\n type: {type(intArr)}\n")

# an array with decimal point numbers 
decArr = arr.array("f", (1.1, 2.2, 3.33))
print(f"decimal type array: {decArr}\n type: {type(intArr)}\n")


"Accessing value from array"

print(f"{intArr[0] = }")

"insert element"

intArr.insert(5, 6) # inserts 6 in index 5
print(f"after updating, {intArr = }")

decArr.append(4.4) # adds 4.4 at last 
print(f"after updating, {decArr = }")

x = arr.array("b", [10, 20, 30])
intArr.extend(x) # extends 2 same type array 
print(f"after updating, {intArr = }")

"removing element"

decArr.remove(decArr[2]) # removes an element
print(f"after removing, {decArr = }")

intArr.pop(6) # removes the element
print(f"after updating, {intArr = }")


"searching element"

print(f"item in index 3 is: {intArr.index(3)}") # returns the element which's index is 3

"updating value"

decArr[1] = 3.14 # changes decArr's 1 to 3.14
print(f"after updating, {decArr = }")

"slicing an array"

print(f"sliced array is: {charArr[:5]}")
print(f"sliced array is: {charArr[7:12]}")

"Copying an array"

newArr = intArr # array copying can be done using assignment operator (shallow copy)
print(f"{newArr=}")

# if changes are made to copy array it'll also be reflected in main array 
newArr[0] = 111
print(f"after updating, {newArr=}")
print(f"after updating the copy array, {intArr = }")

"loop an array"
# simple for loop
for index, value in enumerate(intArr): 
    print(f"item in {index} is: {value}")
    
# for loop with index
for i in range(len(decArr)): 
    print(f"item in index {i} is: {decArr[i]}")

# using while loop
i = 0 # count for loop initialized with 0
while i < len(intArr):
    print(f"item in index {i} is: {intArr[i]}")
    i += 1 # increment the count

"convert array to list"

intList = intArr.tolist()
print(f"{intList = }")

decList = list(decArr)
print(f"{decList = }")

"reversing an array"

# using slice to reverse an array 
print(f"reversed array: {intArr[::-1]}") 

# -> using reverse ()
# as reverse() is a method for list, We need to convert array to list first 
temporayList = intArr.tolist()
temporayList.reverse()
intArr = arr.array("i", temporayList)
print(f"after reversing, {intArr = }")

# -> using reversed()
# reversed() function can take an array as parameter and returns a iterator 
revList = reversed(intArr)
intArr = arr.array("i", revList)
print(f"after reversing, {intArr = }")

"sorting an array"

# -> simple bubble sort
def bubbleSort(array): 
    # loop the array 
    for i in range(len(array)): 
        # now loop from index 1
        for j in range(i + 1, len(array)):
        # if array[i] is greater than array[j], create a temporary var and swap the value 
            if array[i] > array[j]: 
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array
print(f"sorted array: {bubbleSort(intArr)}")
 
# -> using sort() method
# as sort() is a method for list, we need to convert tje array to list first 
tempList = intArr.tolist()
tempList.sort()
intArr = arr.array("i", tempList)
print(f"after sorting, {intArr = }")

# -> using sorted()
# sorted() function can take an array as parameter and returns a iterator 
sortedList = sorted(intArr, reverse = True)
intArr = arr.array("i", sortedList)
print(f"after sorting reversed, {intArr = }")

"joining arrays"

# -> using loop
arr1 = arr.array("i", [1, 2, 3, 4])
arr2 = arr.array("i", [5, 6, 7, 8, 9])
arr3 = arr.array("i", [10, 20, 30])
for elm in arr2: 
    arr1.append(elm) # adds all elements 
print(f"after adding elements, {arr1 = }")

# using extend() method 
arr3.extend(arr2) # extends 2 array 
print(f"after adding elements, {arr3 = }")
