# 68: Methods (and project continued)

import random
class Pound: 

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        # States
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5
        self.thickness = 3.15
        self.heads = True

    def rust(self):
        self.color = "greenish"

    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    #def __del__(self):


coin1 = Pound(rare=True)
coin2 = Pound()

print(coin1.rare)
print(coin2.rare)
print(coin1.value)
print(coin2.value)
print(coin1.color)
coin1.rust()
print(coin1.color)

coin1.flip()
print(coin1.heads)
