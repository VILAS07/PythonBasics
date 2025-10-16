sentences = ["I love Python", "Python is great", "I love coding"]
l=[]
count=[]
for i in sentences:
    for j in i.split(' '):
        if j not in l:
            l.append(j)
        else:
            count[l.index(j)+=1]