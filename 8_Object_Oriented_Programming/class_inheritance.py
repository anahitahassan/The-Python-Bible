# 69/70: Project 10 -- Make all coins.

import random

class Coin:
    def __init__(self, rare = False, clean = True):
        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.calue = self.original_value
        
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color # we'll define these later
    
    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


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

    def __del__(self):
        print("Coin Spent!")