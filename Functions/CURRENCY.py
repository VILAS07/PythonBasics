def inad(c):
    return round(c/22.6,2)

def inud(c):
    return round(c/83,2)




c=int(input('Enter the indian Rupees : '))
print("AED :" ,inad(c))
print("USD :",inud(c))