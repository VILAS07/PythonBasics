p='luminar123'
t=True
c=1
n=2
while t:
    while n<=3:
        a=input('enter the password')
        if n == 0:
            print('profile locked')
            break
        if a==p:
            print('login successful')
            break
        elif a != p or n==0:
            print(f'Incorrect Password you have {n} attempts to enter password ')
            n-=1



    break