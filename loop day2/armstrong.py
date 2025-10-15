n=int(input('enter a number'))
l=len(str(n))
s=0
t=n
for i in str(n):
    r=n%10
    s+=int(i)**l
    n=n//10
if t==s:
    print('armstrong')
else:
    print('not armstrong')




