# 25: Cool String Methods - Part 2

# .index() searches for a given element from the start of the list and returns the lowest index where the element appears 
x = "happy birthday"
print(x.index("birthday"))
# NOTE: there would be an error if you said "Birthday". 

# .find() finds the first occurrence of the specified value. 
# The find () method returns -1 if the value is not found.
print(x.find("p"))
# NOTE: The first character is counted as 0. 

# .strip() returns a copy of the string with both leading and trailing characters removed
y = "0000000000happybirthday00000000000"
print(y.strip("0"))
z = "yyyyyyappybirthdayyyyyyyy"
print(z.strip("y"))

# there's also .lstrip() and .rstrip()
text = "hhhhhhhHappy Birthdayhhhhhhhhh"
print(text.lstrip("h")) # Happy Birthdayhhhhhhhhh
print(text.rstrip("h")) # hhhhhhhHappy Birthday

# len() "length" function returns number of items. 
print(len("hello"))

# read documentation !!!!