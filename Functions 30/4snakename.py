import random
def snakename():
    m=['Angry','Sleepy','Curious']
    s=['Cobra', 'Viper', 'Python']
    return random.choice(m),random.choice(s)
print(snakename())
