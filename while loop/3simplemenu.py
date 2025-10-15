s=1000
while True:
    d=int(input('1 for deposit 2 for withdraw 3 for check balance 4 for exit'))
    if d==1:
        a=int(input('how much you want to deposit'))
        print(f"DEPOSITED {a}")
        s+=a
    elif d==2:
         b=int(input('how much you want to withdraw'))
         print('WITHDRAWED',b)
         s-=b
    elif d==3:
        print(s)
    elif d==4:
        break
