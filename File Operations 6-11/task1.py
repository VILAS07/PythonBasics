import csv
with open('sample_support_tickets-1.txt','r') as obj1:
    a=obj1.readlines()
with open('new.csv','w') as obj2:
    obj2.write('ID,Name,Issue,Priority,Date\n')
    for line in a:
        line=line.strip().split('|')
        c1,c2,c3,c4,c5=line
        obj2.write(f"{c1.split(':')[1].strip()},{c2.split(':')[1].strip()},{c3.split(':')[1].strip()},{c4.split(':')[1].strip()},{c5.split(':')[1].strip()}\n")






