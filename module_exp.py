def avg(*numbers): 
  return sum(numbers) / len(numbers)
  
def info(**user):
  return f"name : {user['name']}\nemail:  {user['email']}\nage  : {user['age']}"
  