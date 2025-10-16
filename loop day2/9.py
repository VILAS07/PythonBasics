cities = ["Kochi", "Thiruvananthapuram", "Calicut", "Kottayam"]
s=""
for i in cities:
    if len(i)>len(s):
        s=i
print(s)