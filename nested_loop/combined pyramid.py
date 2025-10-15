a=4
for i in range(1,6):
    print(' ' * a, end='')
    a -= 1
    for j in range(i):
        print('*', end=' ')
    print()
b=1
for i in range(4,0,-1):
    print(' ' * b, end='')
    b += 1
    for j in range(i):
        print('*', end=' ')
    print()