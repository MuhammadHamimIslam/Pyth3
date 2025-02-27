import random 

lis1 = ["Python", "JavaScript", "C", "Java"] 

n1 = random.randrange(1, 10) # gives a random number from 1 to 10(not included )
print(n1)

n2 = random.random() # gives a random number which is greater than or equal to 0 to 1
print(n2)

n3 = random.choice(lis1) # gives a random number form lis1
print(n3)

n4 = random.shuffle(lis1) # randomize the element in lis1(modifies the list directly)
print(lis1)

n5 = random.randint(1,10) # generates random number between 1 to 10(included)
print(n5)

n6 = random.sample(lis1, k = 2) # returns a new list contains k(2) items randomly 
print(n6)