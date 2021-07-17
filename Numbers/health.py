# 15: PROJECT 1: Crafting a Health Potion
# -------------------------------------------------------------

import random
health = 50 
difficulty = 1 # where hard = 1, medium = 2, easy = 3

# Note: search up 'Python docs Module Index' to read documentation. 
# Alphabetical list of all modules: https://docs.python.org/3/py-modindex.html
# Go to r -> random -> random.randint(a, b)
# "Return a random integer N such that a <= N <= b."
random.randint(10, 20)

potion_health = int( random.randint(25, 50) / difficulty) # dividing by low number makes big number. 
# We imported the random *module* and used the *function* randint. 

health = health + potion_health
print(health)

# As in Java, you can use += to change one variable by adding another variable to it. 

# Casting (putting int and brackets around some code)
