import base64

text = "Hello, Python!".encode() # need to encode in binary format 

base64_encode = base64.b64encode(text) # encodes in base64 in binary format 
print(base64_encode.decode())

base64_decode = base64.b64decode(base64_encode) # decodes the base64 text amd returns in binary format 
print(base64_decode.decode())