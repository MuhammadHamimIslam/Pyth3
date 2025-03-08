"A function to find the number of vowels in a string"

def findVowel(st):
  vowels = "aeiou"
  count = 0
  # check if vowel is present in the string 
  for char in st.lower(): 
    if char in vowels: count += 1 # count increment 
  return count

"A function to convert a string of binary digits to integer"

def convInt(st): 
  for char in st: 
    if char not in "01": return "Invalid string!"
    else: return int(st, 2)

"A function to to sort the characters in a string"

def sortChar(st): 
    return ''.join(sorted(st))

"A function to reverse a string"

strRev = lambda st: st[::-1]

"A function to check palindrome"

def checkPalindrome (st):
  a = st.lower()
  return a == a[::-1]
  
"A function to remove duplicate characters from a string while preserving the order of characters"

def removeDup(st):
  # initial result 
  result = []
  for char in st: 
    if char not in result:
      result.append(char)
  return "".join(result)
  
"A function to count the frequency of each character in a string"

def wordFrequency(st): 
  # initial dictionary 
  result = {}
  for char in st.lower(): # loop inside the string -> case insensitive 
    if char not in result: result[char] = 1
    else: result[char] += 1
  return result

"A function to find the longest word in a given string"

def findLongestWord(st):
  words = st.split(" ") # break str to list 
  result = words[0] # set words[0] = longest 
  for word in words:
    if len(result) < len(word): result = word
  return result

"A function that performs basic string compression using the counts of repeated characters"

def strCompression(st): 
  result = [] # initial result 
  curr = st[0] # current is st[0]
  count = 1
  for i in range(1, len(st)): #loop through string 
    if st[i] == curr: count += 1 # if st[i] matches to current count++
    else:
      result.append(curr) # add current char
      result.append(str(count)) # add current count 
      curr = st[i] # increment the count
      count = 1 # set count to 1
  return "".join(result)

"A function to check if two given strings are anagrams of each other"
def checkAnagram(str1, str2): 
  def wordFrequn(st): 
      # initial dictionary 
    result = {}
    for char in st.lower(): # loop inside the string -> case insensitive 
      if char not in result: result[char] = 1
      else: result[char] += 1
    return result
  return wordFrequn(str1) == wordFrequn(str2)
