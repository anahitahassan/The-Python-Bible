# 60: Keyword Arguments and Default Parameters

def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
    return sentence

print(about("Anahita", 18, "Python"))

print(about(age = 18, name = "Anahita", likes = "Python"))

# print(about("Anahita", 18)) This won't work!

def new_about(name, age, likes = "teaching"):
    sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
    return sentence

print(new_about(name = "Ziyad", age = 29))


# def new_about(name, age = 29, likes):
#     sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
#     return sentence

# This doesn't work because it's a non-default argument (likes) after a default argument (age = 29). 
