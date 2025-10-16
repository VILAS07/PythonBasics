l=[]
for a in range(1,1001):
    for i in range(2,a//2+1):
        if a%i==0:
            break
    else:
        if a>1:
            l.append(a)
print(l)