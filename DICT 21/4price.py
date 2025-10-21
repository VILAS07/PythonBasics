fruits = {"apple": 100, "banana": 40, "orange": 80}
for i,j in fruits.items():
    if i=="banana":
        j+=10
    fruits[i]=j
print(fruits)