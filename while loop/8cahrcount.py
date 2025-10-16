s=input('enter a sentence')
i=0
c=0
while True:
    if s.isalpha():
        i+=1
        c+=1
    elif s[i]==' ':
        i+=1
        c+=1
        continue
    elif s[i]==None:
        break
print(c)

