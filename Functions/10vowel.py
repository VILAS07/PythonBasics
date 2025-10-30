def vow(s):
    c=0
    for i in s:
        if i in ['a','e','i','o','u'] :
            c+=1
    return c

s=input('ether a word')
print(vow(s))