letters = ['a', 'b', 'a', 'c', 'b', 'a']

c = {}
for i in letters:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print(c)


 #OR
 #for i in letters:
    #letters[i]=letters.count(i)