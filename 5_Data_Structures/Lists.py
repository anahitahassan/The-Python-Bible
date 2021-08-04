# 36: Section Overview:
# Data Structures: Lists, Tuples and Dictionaries

# 37: Lists

our_List = [27, 46, -5, 17, 99]
print(our_List)
print(type(our_List))

# you can make lists of multiple types.
jackson = ["A", "B", 1, 2, 3, True, False]
# "A" is at index 0, "B" is index 1, etc. 
print(jackson[0])
print(jackson[-2]) 

#jackson[start:end:step]
print(jackson[0:3])

newList = [1, 2, [3, 4, 5], 6, 7, 8]
print(newList[2])
print(newList[2][0])

# this helps when you make tables! 

ourTable = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ourTable[0][2])

