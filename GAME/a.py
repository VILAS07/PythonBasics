
a=[1, 2, 3, 3, 5]
f=0
d={}
sum = 8
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==sum:
            f=1
            d[a[i]]=a[j]
        else:
            f=0
if f==1:
    print('True')
else:
    print('False')
print(d)
