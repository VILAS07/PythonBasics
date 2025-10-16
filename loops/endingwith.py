fruits=['apple','banana','cherry','mango']
d=input('enter a letter')
for i in range(len(fruits)):
    if fruits[i].endswith(d):
        print(fruits[i])
