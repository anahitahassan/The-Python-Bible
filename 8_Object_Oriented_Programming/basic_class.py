# 65: Section Overview
#   - Learn about objects and classes
#   - Learn how to use class variables and class methods
#   - Learn about class constructors and destructors, class variable and class methods
#   - Model a Coin
#   - Model a Set of Coins
#   - BUild your own Bank

# 66: Objects and Classes
# Objects are instances of classes
# Classes are templates
# Classes are made of States and Methods
# States (of a coin): values, color, diameter, heads
# Methods (of a coin): flip() 

# 67: Project 9: Make your own Coin 
class Pound: 

    # States
    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5
    thickness = 3.15
    heads = True

# out first object/instance
coin1 = Pound()
print(type(coin1))
# <class '__main__.Pound'>

print(coin1.value)

coin1.color = "greenish"
print(coin1.color)

coin2 = Pound()
print(coin2.color)

# notice how the color didn't change this time?
# it's cause coin2 was made new from the Pound template. 
# each object is independent, even though they came form the same class. 