import random
def simulate_savings(balance):
    a=random.randint(500,1001)
    print("+",a if a>0 else -a)
    balance+=a
    return balance
b=100
print(simulate_savings(b))