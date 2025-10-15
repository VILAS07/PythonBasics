a=1
for i in range(5,0,-1):
    print(' ' * a, end='')
    a += 1
    for j in range(i):
        print('*', end=' ')
    print()