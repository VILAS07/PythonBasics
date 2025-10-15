f=0
while True:
    d=input('enter destination')
    if d=='stop':
        print(f)
        break
    else:
        f1 = int(input('enter fare'))
        f+=f1

