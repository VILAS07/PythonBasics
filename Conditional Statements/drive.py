a=input("enter the age")
if a>=18:
    t=input('did you passed test')
    if t=="yes":
        print('eligible for licence')
    elif t=="no":
        print('test not passed')
else:
    print('Too young')