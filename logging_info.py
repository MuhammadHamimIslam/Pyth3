import logging 

def pr(arg): 
    return logging.debug(arg)

# configure basic logging
# the default logging level is 
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")

# a function to add 2 numbers 
def add(num1, num2):
    return f"sum is: {num1 + num2}"
    

pr(add(2, 3))