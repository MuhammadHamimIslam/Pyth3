# argon2 isn't a build-in module
# pip install argon2-cffi
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError # import exception

my_password = "my_secure_password"

# create a password hashing instance
ph1 = PasswordHasher()

pass_hash1 = ph1.hash(my_password) # hash the password 
print("Hashed password = ", pass_hash1)

# verify the password 
try:
    ph1.verify(pass_hash1, my_password) # verify the password with the hashed password 
    print("Password is correct!")
except:
    print("Password is incorrect!")

# customizing the hash
ph2 = PasswordHasher(
    time_cost=3, # number of iteration 
    memory_cost=1024, # memory used in kilobytes
    parallelism=2, # number of threads /CPU cores to use
    hash_len= 30, # length of the hash
    salt_len=15 # length of the random salt 
)

pass_hash2 = ph2.hash(my_password) # hashes the password 
print("Hashed password = ", pass_hash2)

try:
    ph2.verify(pass_hash2, my_password)
    print("Password is correct!")
except VerifyMismatchError: # check if password mismatched 
    print("Password is incorrect!")
except Exception as e:
    print("Some other error occurs ", e)

# check if rehashing is needed 
if ph2.check_needs_rehash(pass_hash2):
    print("Rehashing password")
    pass_hash2 = ph2.hash(my_password)
else:
    print("Password needn't to be rehashed")
    
# example 
users = {}

# register new user
def register(username, password): 
    if username not in users.keys(): 
        users[username] = ph2.hash(password)
        print("Registration successful!")
    else:
        print("User already exists")

# login         
def login(username, password): 
    if username in users.keys(): 
        try:
            ph2.verify(users[username], password)
            print("Login successful!")
        except VerifyMismatchError:
            print("Login failed. Incorrect password")
    else:
        print("User not registered!")

register("John", "j#o#h#n123") # register a user

login("John", "John123###") # try to login with incorrect password 
login("John", "j#o#h#n123")