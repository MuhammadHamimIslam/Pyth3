from typing import List, Dict, Set, Any, Sequence, Optional, Callable

# we can use annotation in any Variable, function for more readability and better documentation

number: int = 100
text: str = "Hello"

# for function 
def addNumbers(a: int, b: int) -> int:
    return a + b
    
# list
ranks: List[int] = [1, 2, 3, 4, 5]

# dictionary 
info: Dict[str, int] = {"a": 10, "b": 20}

# Set
numbers: Set = {1, 2, 3, 4}

# we can create custom data type 
varType = List[Dict[str, float]]

customType: varType = [{"a": 1.1}]

# if any function returns any type we can specify it
def doSomething () -> Any:
    pass

doSomething()

# we can specify that a function can return a Sequence -> str, list, tuple type 
def foo() -> Sequence[str]:
    return "Hello world"
    
foo()

# we also set type to Optional 
def function(param: Optional[int]) -> None: 
    print(param)

function(1)

def multiply(a: int, b: int) -> int: 
    return a * b
# we can also specify type to Callable[[parameterType], returnType]
def test(func: Callable[[int, int], int]) -> None: 
    result = func(10, 20)
    print(result)

test(multiply)

