t=5
while True:
    a=input('you want to book ?')
    if t<=1:
        print('booking ended')
        break
    elif a=='yes':
        print('booked')
        t-=1
        print(t)
    elif a=='no':
        print('booking ended')
        break

