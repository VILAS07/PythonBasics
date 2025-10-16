l=[]
while True:
    a=input('enter a name')
    if a not in l:
        l.append(a)
    else:
        break
print(f"{a} appears 2 times in list")