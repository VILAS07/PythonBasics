data=[5, 10, 15, 20, 25, 30]
l=list(map(lambda a:a*2,filter(lambda a:a%2==0,data)))
print(l)