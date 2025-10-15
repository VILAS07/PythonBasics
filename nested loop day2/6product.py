p = [
    ["John", ["Laptop", "Mouse"]],
    ["Sarah", ["Mouse", "Keyboard"]],
    ["Alex", ["Laptop", "Charger"]]
]

items=[]
names=[]
for i,j in p:
    for item in j:
        if item not in items:
            names.append([])
            items.append(item)
            names[items.index(item)].append(i)
        else:
            names[items.index(item)].append(i)
