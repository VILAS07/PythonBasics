sentence = "Python is simple yet powerful and Python is popular"
t={}
for i in sentence.lower().split(' '):
    if i in t:
        t[i]+=1
    else:
        t[i]=1
print(t)