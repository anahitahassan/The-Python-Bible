# 32: If Statements
num1 = 100
num2 = 50

if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bigger than num1")
else:
    print("num2 is equal to num1")

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