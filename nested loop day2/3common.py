person1 = ["Python", "SQL", "Data Analysis"]
person2 = ["Excel", "Python", "Machine Learning"]
l=[]
for i in zip(person1,person2):
    if i[0]==i[1]:
        l.append(i[0])
print(l)