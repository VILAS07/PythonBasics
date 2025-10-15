store = [
    ["Fruits", ["apple", "banana", "grapes"]],
    ["Snacks", ["chips", "biscuits", "popcorn"]],
    ["Drinks", ["cola", "juice", "water"]]
]
a=input('what you want to search')
for c, i in store:
    if a in i:
        print(f"{a} category: {c[:-1]}")
        break