def find_max(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=10
b=11
c=12
print(find_max(a,b,c))
