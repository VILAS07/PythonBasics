while True:
    j=input('Which juice you want orange, mango, apple')
    if j=='orange'or 'mango' or 'apple':
        print(f"Preparing your {j} juice...")
    elif j=='stop':
        break
    else:
        print('Sorry,Not Available')