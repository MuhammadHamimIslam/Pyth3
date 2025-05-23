import os
from dotenv import load_dotenv # need "pip install dotenv"


load_dotenv() # load the .env file

email = os.getenv("Email") # get data from .env file
print(email)