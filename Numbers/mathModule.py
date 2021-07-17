# 17: Fun with the Python Math Module
# Documentation: https://docs.python.org/3/library/math.html#module-math

# Round function
print(round(2.1)) # 2
print(round(1.5)) # 2 -> what if you wanted .5 to round down?
print(round(1.7)) # 2

import math
print(math.floor(1.5)) # now it's 1!
print(math.ceil(3.1)) # now it's 4! Now if you have .0 how would these functions affect it?
print(math.floor(12.0)) # just 12
print(math.ceil(12.0)) # just 12

# Constants (prints 15 digits after decimal)
print(math.pi) 
print(math.e) 
print(math.tau) 

# Trig functions
print(math.sin( math.pi/2)) # not that we get a float
print(math.sin( math.pi )) # not exactly 0, but if we wanted 0:
print(math.floor( math.sin( math.pi ) ) )

# Hypotenuse
print( math.hypot(3, 4) )
print( math.hypot(5, 12) )

# Power 
print( math.pow(2, 3) )
# Shortcut: 2 ** 3 = 8. 

# Exp and Log
print (math.exp(2) ) 
# math.exp(x): Return e raised to the power x, where e = 2.718281… is the base of natural logarithms.
# This is usually more accurate than math.e ** x or pow(math.e, x).
print( math.log(math.e) ) # recall that math.e is the constant e!
print( math.log10(1000) ) # we get 3 since 10 to power of 3 is 1000. 
print(math.log2(8))

# check out NumPy and SciPi libraries for more advanced math tools!