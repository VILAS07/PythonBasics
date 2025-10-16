f=input('enter your coffie type black/latte/cappuccino')
if f=="latte":
    s=input('which size you want (small,large)')
    if s=="small":
        print('Price = 120')
    elif s == "large":
        print('Price = 150')
elif f=="black":
    print('price = 150')
elif f=="cappuccino":
    print('price = 130')
else:
    print('Item Not Available')