from typing import List, Dict
# we can use annotation in any Variable, function for more readability and better documentation

number: int = 100
text: str = "Hello"

# for function 
def addNumbers(a: int, b: int) -> int:
    return a + b

ranks: List[int] = [1, 2, 3, 4, 5]
print(ranks)

students: Dict = {
    "name": "xyz",
    "age": 16
}

print(students)

