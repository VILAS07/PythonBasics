u='admin'
p='1234'
ug=input('enter used id')
pg=input('enter password')
if u==ug:
    if p==pg:
        print('Login successful')
    else:
        print('wrong password')
else:
    print('invalid username')