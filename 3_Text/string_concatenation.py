# 22: PROJECT 2: Hello You! - Part 1 - Project Overview

A = "part one"
B = "part two"
print(A + B)
print(A + " " + B)
print(A * 3)
print('=' * 20)

B = 2
# print(A + B) -> ERROR !!!!!!!!!
print(A + str(B)) # part one2
# str() converts 2 -> "2"

# Python format function
# {} are like placeholders. 
print("{} - {}".format(A, B)) # part one - 2
print("{} and {} and. ".format(A, B))

# ALSO: A = 0, B = 1, C = 2, D = 3...
A = "aaaaa"
B = "bbbbb"
print("{1} - {0}".format(A, B))

C = "ccccc"
print("{1} - {0} + {2}".format(A, C, B))
# now over here, A = 0, C = 1, B = 2. 
# when 1 is called "ccccc" is printed, when 0 is called "aaaaa" is printed


