from random import randint

class Dice:

    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and the number of side the die has """
        print(randint(1,self.sides))
    


def dice_maker(no_of_sides, no_of_rolls):
    print(f"This Dice has {no_of_sides} sides")
    new_dice=Dice(no_of_sides)
    for roll in range(1,no_of_rolls+1):
        print(f"This is {roll} roll:")
        new_dice.roll_die()

dice_maker(6,10)
dice_maker(10,10)
dice_maker(20,10)