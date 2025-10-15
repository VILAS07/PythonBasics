n=input('enter a word')
for i in range(len(n)):
    if i==0:
        continue
    elif i==len(n):
        continue
    else:
        print(n[i])