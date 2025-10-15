a=input("enter the shopping amount")
if a>=500:
    m=input('are you a member')
    if m=="yes":
        print('20% discount')
    elif m=='no':
        print('10% discount')
else:
    print('no discount')