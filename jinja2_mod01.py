from jinja2 import Environment, FileSystemLoader

env = Environment() # setting the environment for jinja2 

template = env.from_string("Hello, {{ name }}!") # create template {{ placeholder }}
rendered = template.render(name="World") # render with placeholder 

print(rendered)

environment = Environment(loader=FileSystemLoader("templates")) # set environment from the templates folder

template = environment.get_template("tmp1.txt") # set template to the file

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "John",  "score": 100},
    {"name": "Steve", "score": 87},
    {"name": "Alexander", "score": 92},
]
for student in students:
    content = template.render(
        student, # pass the list to render 
        max_score=max_score,
        test_name=test_name
    )
    print(content)
    print("-" * 58)