n=int(input('enter a number'))
s=0
for i in str(n):
    r=n%10
    s+=r
    n=n//10
print(s)



