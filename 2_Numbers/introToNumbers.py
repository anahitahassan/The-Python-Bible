# Videos 12-15 
# Topics: control order of computations, learn about floats, using External Python Modules
# First project: make a ehalth potion for a video game 
# Python math module: rounding, powers, square roots, basic trig, more advanced topics

# 13: Basic Arithmetic, Floats and Modulo
# -------------------------------------------------------------
# We know: + , - , * , /
print(type(2)) # <class 'int'>
print(type(0.5)) # <class 'float'>
# float takes up 16 bytes, int is 14
# Modulo: allows us to find remainder, it's the same in java. 
print(5 % 3)
print(10 % 2)
print(7.5 % 5) # 5 goes into 7.5 once, with 2.5 left over. 
print(15 % 2.5)
print(type(15 % 2.5)) # 0.0 is float

# 14: Ordering Operations using (Brackets!)
# -------------------------------------------------------------
print(2 + 5 * 4) # 22; it follows PEMDAS! it doesn't just go L->R
print((2 + 5) * 4) # 28 because we used brackets. 


