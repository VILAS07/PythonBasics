def Currency(v,c):
    if c.lower()=='aed':
        return round(v/22.6,2)
    elif c.lower() == 'usd':
        return round(v / 83, 2)





v=int(input('Enter the indian Rupees : '))
c=input('Enter the currency like usd , aed  : ')
print(Currency(v,c))