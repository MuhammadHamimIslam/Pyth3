"Generators in Python are a convenient way to create iterators"

"generator using function"

def generator(start, stop, step=1): 
    current = start 
    while current < stop:
        yield current 
        current += step

# using generator 

for i in generator(1, 5): # iterate over a generator 
    print(i)
    
"Using generator expression"

gen = (i ** 2 for i in range(1, 5))

print("next is", next(gen)) # get the next item

for i in gen: 
    print(i)

"Exception handling of generator"

itr = generator(1, 10, 2)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break
    
    