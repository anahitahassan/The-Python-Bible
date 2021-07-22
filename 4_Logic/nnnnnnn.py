# 30: Section Overview
#   - Boolean Datatype
#   - Conditional Operators
#   - If / if-else statements
#   - Logical Keywords

# 31: Booleans & Comparison Operators
d = True
e = "True"
print(type(d)) # <class 'bool'>
print(type(e)) # <class 'str'>

print(2 > 3)
print(3 > 2)
print(type(2 < 3))

# note: you can't use '=', it must be '=='
print(2 == 3)
print(3 == 3)

print(4 >= 3)
print(2 >= 3)

# 32: If Statements
num1 = 100
num2 = 50

if num1 > num2:
    print("num1 is bigger than num2")