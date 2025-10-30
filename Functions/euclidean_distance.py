def ED(x1,y1,x2,y2):
    a=((x2-x1)**2) + ((y1-y2)**2)
    return a**0.5

x1=int(input('enter x1 value'))
y1=int(input('enter y1 value'))
x2=int(input('enter x2 value'))
y2=int(input('enter y2 value'))
print(ED(x1,y1,x2,y2))