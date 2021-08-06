# 58: Variable Scope

a = 100
def f1(): 
    return a
def f2():
    return a

print(f1())
print(f2())

# In this example, 100 was printed for both since a = 100 is on the outside

def f1(): 
    a = 200
    return a
def f2():
    return a

print(f1())
print(f2())
print(a)

# In this last example, 200 and 100 are printed because a = 200 is only within the scope of f1. 
# When we just print a, it's 100 since a = 100 is established as a global variable instead of the local variable a = 200 within the scope of f1. 


