students = {
    "A101": {
        "name": "Anjali",
        "age": 17,
        "gender": "Female",
        "marks": {
            "Math": 78,
            "English": 82,
            "Science": 69
        }
    },
    "A102": {
        "name": "Rahul",
        "age": 16,
        "gender": "Male",
        "marks": {
            "Math": 55,
            "English": 60,
            "Science": 58
        }
    },
    "A103": {
        "name": "Meera",
        "age": 17,
        "gender": "Female",
        "marks": {
            "Math": 91,
            "English": 87,
            "Science": 93
        }
    },
    "A104": {
        "name": "Arjun",
        "age": 16,
        "gender": "Male",
        "marks": {
            "Math": 44,
            "English": 39,
            "Science": 51
        }
    },
    "A105": {
        "name": "Diya",
        "age": 17,
        "gender": "Female",
        "marks": {
            "Math": 72,
            "English": 70,
            "Science": 65
        }
    }
}
s=0
for i,j in students.items():
   print(f"{j['name']} --> Average :{sum(j['marks'].values())/len(j['marks'].values())}")


for j in students.values():
    if min(j['marks'].values())<50:
       print(j['name'],'FAILED',j['marks'])

s=0
c=0
for i,j in students.items():
    if j['gender']=='Male':
        c+=1
        s+=j['marks']['Math']
print(f'Average Math Score for Male Students is {s/c}')
s=0
c=0
for i,j in students.items():
    if j['gender']=='Female':
        c+=1
        s+=j['marks']['Math']
print(f'Average Math Score for Female Students is {s/c}')


t=0
c=''
for i,j in students.items():
    if j['marks']['Science']>t:
        t=j['marks']['Science']
        c=j['name']
print(t,c)

import random
for i,j in students.items():
    j['marks']['computer']=random.randint(60,90)
print(students)



