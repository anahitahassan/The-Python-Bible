# 68: Methods (and project continued)

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

coin1 = Pound(rare=True)
coin2 = Pound()

print(coin1.rare)
print(coin2.rare)
print(coin1.value)
print(coin2.value)
print(coin1.color)
coin1.rust()
print(coin1.color)


# I stopped at video 68 at time 8:06 minutes