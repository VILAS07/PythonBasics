juices = ["Mango Juice", "Apple Juice", "Banana Juice", "Orange Juice", "Pineapple Juice"]
s = 'Remove banana juice, it tastes weird.'
l = s.lower().split()
n = []
print(l)
for i in juices:
    a = i.split()[0].lower()
    if a not in l:
        n.append(i)
juices = n
print(juices)
