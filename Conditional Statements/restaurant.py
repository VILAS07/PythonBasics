f=input('enter youe food choice')
if f=="Pizza":
    s=input('which size you want (small,medium,large)')
    if s=="small":
        print('Price = 150')
    elif s=="medium":
        print('Price = 250')
    elif s == "large":
        print('Price = 350')
elif f==Burger:
    vn=input("veg or non_veg")
    if vn=="veg":
        print('price = 100')
    elif vn=="non_veg":
        print('price = 150')
else:
    print('Item Not Available')