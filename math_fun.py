import math

n1 = math.ceil(10.0001)
print(n1) # ceils the floating point number 

n2 = math.comb(5, 3) # returns nCr = 5C3
print(n2)

n3 = math.copysign(5, -1) # returns -5.0 
print(n3)

n4 = math.fabs(-10) # gives absolute value
print(n4)

n5 = math.factorial(6) # returns factorial 
print(n5)

n6 = math.floor(10.9999) # floors a floating point number 
print(n6)

n7 = math.fmod(10,3) # returns modulas (%)
print(n7)

n8 = math.isclose(10, 10, rel_tol= 0.1) # checks if 2 numbers is close 
print(n8)

n9 = math.pow(2, 5) # returns param1 ^ param2
print(n9)

n10 = math.sqrt(4) # returns square root (✓)
print(n10)

n11 = math.cbrt(27) # returns cube root ³✓
print(n11)

n12 = math.log(1e4, 10) # returns log
print(n12)

n12 = math.sin(1) # returns sine (radian)
print(n12)

n13 = math.cos(-1) # returns cosine (radian)
print(n13)

n14 = math.tan(1) # returns tangent (radian)
print(n14)

n15 = math.degrees(math.pi) # converts radian to degree 
print(n15)

n16 = math.radians(180) # converts degree to radian 
print(n16)

# build in method 

print(abs(-10)) # returns absolute value 

print(pow(2,5)) # returns power 2^5

print(round (9.99) # rounds a float 
