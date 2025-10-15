colors=['red','blue','green','blue']
for i in range(len(colors)):
    if 'blue' in colors:
        a=colors.index('blue')
        colors.remove(colors[a])
        colors.insert(a,'skyblue')
print(colors)



