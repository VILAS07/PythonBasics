def prime(a):
    c=0
    for i in range(1,a):
        if a%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False

a=int(input('enter the number'))
print(prime(a))