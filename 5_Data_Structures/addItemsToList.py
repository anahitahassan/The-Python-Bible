# 41: More ways to add items to lists.

a = [1, 12, 13, 15, 62]
a = a + [4]
print(a)

a = a + ["BCD"]
print(a)

a = a + [1, 2, 3, 4]
print(a)

a = a + list("BCD")
print(a)

a = a + list(str(123))
print(a)

a.append("HEYYYYY")
print(a)

a.remove(1) # this is removing the value '1', NOT THE INDEX.
print(a)