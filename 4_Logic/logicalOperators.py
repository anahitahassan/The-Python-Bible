# 33: Python Logical Operators - Part 1 - not + and
print(not True)
print(not 2 < 3)

x = 10
y = 20
if not y < x:
    print("it worked!")

# "Not" Truth Table:
# A = 0 (false) -> Output: 1 (true)
# A = 1 (true)  -> Output: 0 (false)

# "And" Truth Table: 
# A = 0 and B = 0 -> Output: 0
# A = 0 and B = 1 -> Output: 0
# A = 1 and B = 0 -> Output: 0
# A = 1 and B = 1 -> Output: 1

C = 10
D = 5
if C > 10 and D > 1:
    print("it worked, yay") # not printed, since 10 > 10 is false

if C >= 10 and D > 1:
    print("it worked, yay")

if not (C > 10 and D > 1):
    print("it worked, yay") # prints. 


# 34: Python Logical Operators - Part 2 - or operator
# "Or" Truth Table: 
# A = 0 and B = 0 -> Output: 0
# A = 0 and B = 1 -> Output: 1
# A = 1 and B = 0 -> Output: 1
# A = 1 and B = 1 -> Output: 1
# if one of the two is True(1), the whole thing is true. 

X = 5
Y = -1
if X > 1 or Y > 1:
    print("it worked, again.")
if (X > 5 and Y > 5) or (X > 1 and Y > 1):
    print("oooh lets see if this prints")
if not ((X > 5 and Y > 5) or (X > 1 and Y > 1)):
    print("oooh lets see if this prints")

# 35: Section Review: im done now yayyyyyyy