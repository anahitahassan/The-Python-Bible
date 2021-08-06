# 61: Packing and Unpacking using *args and *kwargs

# Unpacking: 

print(1, 2, 3, 4, 5)
# 1 2 3 4 5

numbers = [1, 2, 3, 4, 5]
print(numbers)
# [1, 2, 3, 4, 5]

print(*numbers)
# 1 2 3 4 5

print("abc") # abc
print(*"abc") # a b c

def add(x, y):
    return x + y

print(add(10, 10))

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like{}.".format(name, age, likes)
    return sentence

dictionary = {"name": "Ziyad", "age": 23, "likes": "Python"}
print(about(**dictionary))

def foo(**kwargs):
    for key, value in kwargs.item():
        return ("{} : {}".format(key, value))

foo(huda = "Female", ziyad = "Male")
print(foo)