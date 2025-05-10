"collections module has some data types like namedtuple, deque, ordereddict, "
from collections import namedtuple

"namedtuple -> namedtuple(name, 'values') "
# named tuple means a tuple where tuple has name like index
Point = namedtuple("Info", "Name, Email, ID_No")
tpl1 = Point("Abc", "abc@email.com", "abc1o1") # parameter passed as key

print(f"The namedtuple is: {tpl1}")

for  index, value in enumerate(tpl1): # can be iterated through loop
    print(index, value)
    
print(tpl1[0]) # can be accessed using index
print(tpl1.Name) # can be accessed using name

print(tpl1._asdict()) # convert namedtuple to ordered dictionary 

d = {"Name": "abc", "Email": "abc@email.com", "ID_No": "pqr"}
tpl2 = Point(**d) # convert from a dictionary
print(tpl2)

tpl2._replace(ID_No="abc108")
print(tpl2)