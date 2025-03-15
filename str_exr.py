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
    return int(st, 2)

"A function to to sort the characters in a string"

def sortChar(st): 
    return ''.join(sorted(st))

"A function to reverse a string"

strRev = lambda st: st[::-1]

"A function to check palindrome"

def isPalindrome (st):
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
  result.append(curr)  # add last character
  result.append(str(count))  # add last count
  return "".join(result)

"A function to check if two given strings are anagrams of each other"
def isAnagram(str1, str2): 
  def wordFrequn(st): 
      # initial dictionary 
    result = {}
    for char in st.lower(): # loop inside the string -> case insensitive 
      if char not in result: result[char] = 1
      else: result[char] += 1
    return result
  return wordFrequn(str1) == wordFrequn(str2)

"A function to encrypt a given string by shifting each character by a certain number of positions in the alphabet."

def caesarCipherEncrypt(inpStr, shift): 
  result = ""
  for char in inpStr: 
    if char.isalpha():
      if char.islower(): 
        start = ord('a')
      else:
        start = ord('A')
      shiftedChar = chr((ord(char) - start + shift) % 26 + start)
      result += shiftedChar
    else:
      result += char
  return result

"A function to decrypt a Caesar encrypted string by shifting each character by a certain number of positions in the alphabet."

def caesarCipherDecrypt(inpStr, shift): 
  result = "" # an empty string to hold the value 
  for char in inpStr: # interate through the string 
    if char.isalpha(): # if char is a character 
      if char.islower(): 
        start = ord("a")
      else:
        start = ord("A")
      shiftedChar = chr((ord(char) - start - shift) % 26 + start)
      result += shiftedChar
    else:
      result += char
  return result
  
"A function to swap the case of all characters in a string"

def swapCase(inpStr): 
  result = "" # empty string to store 
  for char in inpStr: #loop the str
    if char.islower(): # if lower -> upper 
      result += char.upper()
    else: # if upper -> lower 
      result += char.lower()
  return result 

"A function to remove all punctuation from a string"

def removePunc(inpStr):
  result = "" # empty string 
  punctuation = "'.,/-_(!?\")" # all punc
  for char in inpStr: # loop the str
    if char not in punctuation: # if punctuation isn't present then add the char to the result 
      result += char
  return result


  

"A  function to find all unique characters in a string"

def findUniqueChar(inpStr): 
  tracker = {} # word tracker 
  for char in inpStr.lower(): # case insensitive loop
    if char not in tracker: 
      tracker[char] = 1 # if eord not in tracker word will be added 
    else:
      tracker[char] += 1 # word count++
  uniqueChar = [char for char in tracker if tracker[char] == 1] # find unique chars
  return uniqueChar

"A function to check if a substring exists within a given string"  

isSubStr = lambda inpStr, subStr: subStr in inpStr

"A function to encrypt a string with ROT13"

def rot13(text):
  result = []
  for char in text: 
    if char.islower(): 
      result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
    elif char.isupper():
      result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
    else:
      result.append(char)
  return "".join(result)
  
