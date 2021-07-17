# 17: Fun with the Python Math Module
# Documentation: https://docs.python.org/3/library/math.html#module-math

# Round function
print(round(2.1)) # 2
print(round(1.5)) # 2 -> what if you wanted .5 to round down?
print(round(1.7)) # 2

import math
print(math.floor(1.5)) # now it's 1!
print(math.ceil(3.1)) # now it's 4!

# Constants (prints 15 digits after decimal)
print(math.pi) 
print(math.e) 
print(math.tau) 

# Trig functions
print(math.sin( math.pi/2)) # not that we get a float
print(math.sin( math.pi )) # not exactly 0, but if we wanted 0:
print(math.floor( math.sin( math.pi ) ) )

# Hypotenuse
print( math.hypot(3, 4))
print( math.hypot(5, 12))

# Power
print( math.pow(2, 3))
