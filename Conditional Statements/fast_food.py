p=input("enter food combo choice 1,2,3")
if p=="1":
    print("Burger + Coke = 120")
elif p=="2":
    print('Pizza + Fries = 250')
elif p== "3":
    v=input('veg or non_veg')
    if v=="veg":
        print('price = 300')
    elif v=="non_veg":
        print('price = 350')
else:
    print("Invalid Combo")
