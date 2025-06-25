import hashlib

text = b"Hello, World"

# hashing using hashlib.sha256()

h1 = hashlib.sha256() # instantiate a hash sha256
h1.update(text) # hashes the text (should be binary format )
hashed_hx1 = h1.digest() # get the hashed in hexadecimal format 
hashed_text1 = h1.hexdigest() # get the hashed as text

# using hashlib.new()

h2 = hashlib.new("sha256") # instantiate a hash sha256

h2.update(text) # hashes the text (should be binary format )
hashed_hx2 = h2.digest() # get the hashed in hexadecimal format 
hashed_text2 = h2.hexdigest() # get the hashed as text

print(hashed_hx1)
print(hashed_text1)

print(hashed_hx2)
print(hashed_text2)

print(hashlib.algorithms_guaranteed) # prints all guaranteed hashing algorithms 
print(hashlib.algorithms_available) # prints all guaranteed available algorithms 

print(h1.digest_size) # returns The size of the resulting hash in bytes
print(h1.block_size) # returns The internal block size of the hash algorithm in bytes

# hashing a file 
with open('hashlib_mod.py', 'rb') as f: # open file as read binary format 
    dg = hashlib.file_digest(f, "sha256") # hash the file with sha256
print(dg.hexdigest()) # prints tje hashed text