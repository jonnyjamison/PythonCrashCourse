import random

class Die():

    def __init__(self,no_of_sides):

        self.no_of_sides = no_of_sides

    def roll(self, no_of_rolls):

        for i in range(no_of_rolls):

            roll = random.randint(1, self.no_of_sides)

            print(f"{self.no_of_sides} sided dice rolled {roll}")



six_sided = Die(6)

six_sided.roll(3)
