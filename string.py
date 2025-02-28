x = "Hello World!"

print(len(x)) # gives the length of string 
print(x.upper()) # upper all the characters 
print(x.lower()) # lower all the characters 
print(x.capitalize()) # capitalize the 1st character
print(x.casefold()) # lower the 1st character
print(x.count("l")) # find l is present how many times 
print(x.startswith("Hell")) # checks if it starts with "Hell"
print(x.endswith("ld!")) # checks if it ends with "ld!"
print(x.find("Hell")) # finds the index of H
print(x.replace("World", "Everyone")) # replaces World with Everyone
print(x.index("!")) # gives the index of "!"
print(x.split(" ")) # breaks the string to list with " "
print("       Hello     ".strip()) # removes whitespace 
print("123".isdigit()) # returns true is all elements ate digits 
print("    Hey  ".lstrip()) # removes whitespace from left
print("  Hey everyone   ".rstrip()) # removes whitespace from right 


# string slicing 
print(x[11]) # returns the character of i 12
print(x[0:5]) # returns the string from index 0 to 5 but 5 not included 
print(x[6:]) # returns the string from index 6 to last
print(x[:5]) # returns the string from first to 5 but 5 not included
print(x[-1]) # returns the last character 

