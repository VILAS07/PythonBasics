import random
def lovecalc(n1,n2):
    a=random.randint(1,101)
    if a<40:
        return 'Maybe better friends'
    elif a<=80 and a>=40:
        return 'Somthing s Cooking'
    else:
        return 'PERFECT MATCH'

name1=input('Enter the name ')
name2=input('Enter the name ')
print(lovecalc(name1,name2))
