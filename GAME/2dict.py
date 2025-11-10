
# 👉 {'A': +5, 'B': -2, 'C': +15

before = {"A": 10, "B": 20, "C": 30}
after = {"A": 15, "B": 18, "C": 45}
d={}
for i  in before:
    a=after[i]-before[i]
    d[i]=f"+{a}"if a>0 else a
print(d)
