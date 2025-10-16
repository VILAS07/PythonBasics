a=7
z=True
i=0
while z:
    i=int(input('Guess the number (unlimited chance) : '))
    if i==a:
        print('Congradulations u guesses the right number')
        z=False
    elif i>a:
        print('Too High')
    else:
        print('Too Low')
