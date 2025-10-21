keys = ['name', 'age']
values = ['Anu', 25]
t={}
for i,j in zip(keys,values):
    t[i]=j
print(t)

#print(dict(zip(keys,values)))