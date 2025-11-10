with open('data.csv','a') as obj:
    obj.write('Name, Age, Place\n')
    while True:
        res=input('do you want to enter data yes / no')
        if res in ['n','no']:
            break
        name=input('enter your name : ')
        age = input('enter your age : ')
        place = input('enter your place : ')
        obj.write(f'{name},{age},{place}\n')