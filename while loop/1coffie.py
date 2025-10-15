t=True
n=int(input('many cups of coffie you drank today'))
while t:
    c=input('do you want another cup of coffie')
    if c.lower()=='yes':
        n+=1
    elif c.lower()=='no':
        print(f"total number of cups today : {n}")
        break
    