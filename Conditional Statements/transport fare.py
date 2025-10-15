v=input('enter a vehicle type eg : bus,train,flight')
if v=="bus":
    print("price = 500")
elif v=='train':
    w=input("enter which class slepper or AC")
    if w=="slepper":
        print('price = 700')
    elif w=="AC":
        print('price = 1200')
elif v=='flight':
    f=input("enter which class economy or business")
    if f=="economy":
        print('price = 5000')
    elif f=="business":
        print('price = 12000')
else:
    print('Invalid Choice')

