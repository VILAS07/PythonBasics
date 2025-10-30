def discounted_price(price, discount_percent):
    return price-(price*discount_percent)



p=int(input('enter the prize'))
d=float(input('enter the discount percentage'))
print(discounted_price(p,d))