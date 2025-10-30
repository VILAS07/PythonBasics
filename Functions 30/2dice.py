import random


def roll_dice():
    l=[1,2,3,4,5,6]
    return random.choice(l)

a=roll_dice()
b=roll_dice()
print(f"You rolled {a} and {b}! Total = {a+b}")