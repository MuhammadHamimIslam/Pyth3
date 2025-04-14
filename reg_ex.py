import re

# A regular expression is a sequence of character to perform search pattern 

"""re class has several function:
    re.search()
    re.findall()
    re.split()
    re.sub()
    """

text = "Bangladesh is the most beautiful county in the world"

# now search pattern 
" '^text' -> starts with text"
x = re.findall("^Bangladesh.*world$", text)

print(x)

