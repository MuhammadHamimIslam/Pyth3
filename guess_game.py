import random 

num1 = int(input("Enter your minimum value:"))
num2 = int(input("Enter your maximum value: "))

rand = random.randrange(num1, num2)
attempt = 0

while attempt != 3:
  guessedNum = int(input(f"guess your number between {num1} to {num2}:"))
  if guessedNum == rand:
    print("You nailed it")
    break
  else:
    print("Number not natched! Try again")
    attempt += 1
else:
  print(f"You couldn't guess the number! It's {rand}")
