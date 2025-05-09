from string import Template 

"Template.substitute()"

"-> using positional argument"

tmp = Template("Hey $name. As you're $age years old, You're welcome!") # creating Template 
new_str1 = tmp.substitute(name="xyz", age=25) # then tmp.substitute(templateArgument)
print(new_str1)

"-> using dictionary"

dct = {"name": "abc", "age": 28}
new_str2 = tmp.substitute(dct) # if any parameter isn't found, it'll raise an error 
print(new_str2)

"-> using safe_substitute"

my_dict = {"name": "pqr"} # missing age
new_str3 = tmp.safe_substitute(my_dict)
print(new_str3)

