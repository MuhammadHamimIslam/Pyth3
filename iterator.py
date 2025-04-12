# An iterator is an object that contains a countable number of values.
# we can iterate over a string, tuple, list, dictionary. That's mean they're iterable object 
myTuple = ("variable", "loop", "function", "condition", "object")
myIterator = iter(myTuple) # returns an iterator from the tuple 
print(next(myIterator)) # we can get the next element by using next() function 
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# create an iterator
class numbers:
    def __init__(self, start, stop, step=1):
        # set property 
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self): # __iter__() function to create the iterator 
        self.curr = self.start # first count start from start properly 
        return self # now return this
    def __next__(self):
        if self.curr <= self.stop: 
            x = self.curr
            self.curr += self.step # increment of count 
            return x # return the current 
        else:
            raise StopIteration 
    
clas = numbers(1, 5)
myiter = iter(clas)

for i in myiter: 
    print(i)