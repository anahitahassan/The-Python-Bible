# 59: Variable Scope Part 2

a = 250 

def function1():
    global a
    a = 100 # global
    return a

def function2(): 
    a = 50 # local
    return a

print(function1()) # 100
print(function2()) # 50
print(a) # 100 (even though we said 250 earlier)

# when you use global keyword it overrides everything

