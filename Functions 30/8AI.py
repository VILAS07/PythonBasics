import random


def fun_ai():
    n=["Chat", "Code", "Logic", "Neural", "Brain", "Data", "GPT", "Smart", "Lazy", "Hyper", "Quantum", "Mega", "Bot", "Coder", "Byte", "Think", "Vision", "Mind", "Talk", "Synth"]
    c=["-LOL-9000", "-2.5", "-404", "-X", "-AI", "-3000", "-V2", "-BETA", "-NEXT", "-ZERO", "-ULTRA", "-V5", "-LITE", "-V99", "-ALPHA"]
    return random.choice(n),random.choice(c)

a,b=fun_ai()
print(a,b)