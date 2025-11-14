class Student:                             #CLASS
    def __init__(self,id,name,age,mark):   #CONSTRUCTOR
        self.id=id                         #PROPERTIES
        self.name=name
        self.age=age
        self.mark=mark

Student1=Student(1,'Vilas',22,100) #OBJECT
print(Student1.id)                                       #BEHAVIOUR
print(Student1.name)
print(Student1.age)
print(Student1.mark)

