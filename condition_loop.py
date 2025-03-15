a = int(input("Enter the number: "))

if a % 2 == 0: 
  print("Even!")
else:
  print("Odd!")

"shorthand approach"
print("Even") if a % 2 == 0 else print("Odd")

if a > 0: 
  print("positive!")
elif a == 0:
  print("Zero!")
elif a < 0:
  print("negative!")
  
"Shorthand approach"
print("positive!") if a > 0 else print("Zero!") if a == 0 else print("negative")

"for loop"

for i in range(0, 6): 
  print(i) # prints the number between 0 to 6 exclusive 
for _ in range(0, 6): 
  print("I'm inside the loop")
  
"while loop"

while a > 10 : # continue loop till the condition is false 
  print("A is less than 10!")
  a += 1
else:
  print("done!")