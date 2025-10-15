fruits=['apple','pineapple','kiwi','strawberry','fig']
s=0
for i in range(len(fruits)):
    if len(fruits[i])>=5:
        s+=1
print(s)