import re

# A regular expression is a sequence of character to perform search pattern 

text = "Bangladesh is the most beautiful county in the world"

# now search pattern 
" '^text' -> starts with text"
x = re.search("^Bangladesh.*world$", text)

print(x)