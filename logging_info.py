import logging 

# configure basic logging
# the default logging level is warning
# we can format the logging using format = "%(asctime)s" for time "%(levelname)s for seeing the level %(message)s to see the message"

logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s", filename = "x.log")

# a function to add 2 numbers 
def add(num1, num2):
    return f"sum is: {num1 + num2}"
    

logging.debug(add(2, 3))

"customizing logging"

# create a logger 
logger = logging.getLogger("my_app")
# set level to debug 
logger.setLevel(logging.DEBUG)

# create console handler and set log level to debug
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# create formatter 
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# add console handler to logger
logger.addHandler(handler)


logging.debug("Let's debug")