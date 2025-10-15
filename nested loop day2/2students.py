students = [
    ["Alice", [78, 82, 91]],
    ["Bob", [65, 79, 72]],
    ["Cathy", [88, 90, 67]]
]
for i , j in students:
    for k in range(0,len(j)-1):
        if j[k]>80:
            print(f"{i} Passed")
        else:
            continue
