# Last section, we made our first python script, but how can we save the results? 
# Variables all have a uniquely identifiable name. 
# A Variables has a name and a certain value. 
number = 12
print(number)
# When I tried to run this, I ran into an error. It was cause I had ")" in my folder name "1)Variables"
# Now I know not to use ")" and other similar symbols in folder/file names. 

# print(Number)
# This doesn't work since Python is all case sensitive!

# Python is a dynamically typed language
# Each variable can have a certain type and you can find that by using what's called the type function. 
print(type(number))
# '<class 'int'>' is printed. 
# The type of our variables can change
# This is different from statically typed languages like C or Java,
# In Java you need to define the type of variable when you create it; in Python you dont!
number = "hello"
print(type(number))
# Now it says: <class 'str'>, as expected. 

