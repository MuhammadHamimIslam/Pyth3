import re

# A regular expression is a sequence of character to perform search pattern 

"""re class has several function:
    re.search(pattern, text, flag=0)
    re.findall(pattern, text, flag)
    re.split()
    re.sub(pattern, replaceText, text)
"""

email = input("Enter your text here: ")

# now search pattern 
" ^ -> starts with"
" . -> any character"
" $ -> ends with "
" + -> one or more occurance"
" * -> zero or more occurance"
" (...) -> specify group "
" A|B -> checks for A or B"
" [anything] -> checks for the characters in the square bracket"
" [^something] -> checks for characters except something in the square bracket"

"""
some special formats for patterns 

\w -> [a-zA-Z0-9_] (word characters only)
\W -> except word characters
\s -> space
\S -> noy space
\d -> 0-9 (decimal values )
\D -> except decimal values 

"""

if re.search(r"^\w+@\w+\.(com|edu|net|gov)$", email, re.IGNORECASE): # means the email should be start with some word characters then @ then some word characters and end with .com or edu or gov and it'll ignore case sensitivity 
    print("Valid")
else:
    print("Invalid")


