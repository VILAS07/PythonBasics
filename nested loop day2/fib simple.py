l=[0,1]
n=int(input('enter a number'))
for i in range(n-2):
    l.append(l[-1]+l[-2])
print(l)