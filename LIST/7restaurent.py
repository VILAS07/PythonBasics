from os import remove

l=['Burger', 'Pasta', 'Pizza']
while True:
    c=input('chef which you completed')
    if c  in l:
        print(f'chef completed : {c}')
        l.remove(c)

    if not l:
        print('All orders Served')
        break
print(l)
