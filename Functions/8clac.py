def cal(a,b,o):
    if o=='+':
        return a+b
    elif 0=='-':
        return a - b
    elif 0 == '*':
        return a * b
    elif 0 == '/':
        return a / b
    elif 0 == '%':
        return a % b
    else:
        return None
a=int(input('enter the number'))
b=int(input('enter the number'))
o=input('enter the operator')
print(cal(a,b,o))