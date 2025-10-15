pin="1234"
p=input("enter PIN")
if p==pin:
    a=int(input('enter the amount'))
    if a<=10000:
        print('withdrawal Successful')
    else:
        print('limit exceeded')
else:
    print('Invalid PIN')