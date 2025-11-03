data=[10, 15, 20, 33, 40, 55]
l=list(filter(lambda a:a%2==0 and a%5==0,data))
print(l)