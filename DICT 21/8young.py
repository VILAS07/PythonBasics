ages = {"Rahul": 21, "Neha": 23,"Arjun": 20,}
for i,j in ages.items():
    if j==min(ages.values()):
        print(i,j)