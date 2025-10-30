import random
def today_mood():
    l=["Happy", "Sleepy", "Hungry", "Motivated", "Confused", "Coder Mode: ON"]
    return random.choice(l)
print(today_mood())