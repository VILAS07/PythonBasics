com=['Indian Oil','State Bank of India','Tata Motors']
s=''
for i in range(len(com)):
    for j in com[i]:
        if j.isupper():
            s+=j
        else:
            continue
    print(s,end=',')
    s=''

