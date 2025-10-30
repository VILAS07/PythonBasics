import random
def what_to_eat():
    a=["Pizza", "Burger", "Salad", "Ice Cream", "Tacos"]
    a = random.choice(a)
    if a.lower()=='salad':
        print('why are you healthy today')
        return a
    else:
        return a

print(what_to_eat())