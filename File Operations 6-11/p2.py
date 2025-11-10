import csv

with open('data.csv','r') as obj1:
    res=csv.DictReader(obj1)
    for i in res:
        if i['Name']=='vilas':
            print(i[' Place'])