x=[1,2,3]
y=[4,5,6]
l=[(x[i],y[j]) for i in range(0,len(x)) for j in range(len(y)) ]
print(l)