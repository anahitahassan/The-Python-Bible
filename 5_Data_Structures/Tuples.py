# 42: Tuples

# Similar to lists, but they can't be changed once created.

ourTuple = 1, 2, 3, "A", "B", "C"
print(type(ourTuple))

print(ourTuple[0:3])
# you will get an error if you say: ourTuple[2] = 100

# tuples are good for when you have data you want to protect and remain unchanged.