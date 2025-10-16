b=0
while True:
    a=input('how much to recharge : ')
    if a=='done':
        break
    else:
        print('recharged : ',a)
        b+=int(a)
        print('balance : ',b)