def fact(n):
    f=1
    for i in range(n,1,-1):
        f*=i
    return f


n=(int(input('enter the number')))
print(fact(n))