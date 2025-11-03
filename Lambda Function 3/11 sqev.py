data=[3, 6, 8, 11, 14, 17]
r=list(map(lambda a:a**2,filter(lambda a:a%2==0,data)))
print(r)