students = ["Anu", "Rahul", "Meera", "Arya", "Jithin"]
ab=['Rahul','Arya']
present=[]
for i in students:
    for j in ab:
        if i==j:
            students.remove(j)
print(students)
