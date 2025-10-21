marks = {'Arun': 65, 'Binu': 80, 'Charu': 72}
t=0
for i in marks.values():
    if i>t:
        t=i
for i,j in marks.items():
    if j==t:
        print(i,t)