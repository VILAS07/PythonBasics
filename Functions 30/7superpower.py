import random
def get_superpower(name):
    p=["Invisibility", "Flying", "Mind Reading", "Super Strength", "Talking to Code"]
    return random.choice(p)
n=input('enter the name : ')
print(n,"power : ",get_superpower(n))