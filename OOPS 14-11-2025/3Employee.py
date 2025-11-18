class Employee:
    def __init__(self,Name,Position,Salary):
        self.name=Name
        self.position=Position
        self.salary=Salary
    def apply_raise(self,percentage):
        self.salary=self.salary + (self.salary * (percentage / 100))
        print(f'Your Salary is increased by {percentage}% : {self.salary + (self.salary * (percentage / 100))}')
    def display_info(self):
        print(f'Employee Name : {self.name}')
        print(f'Position : {self.position}')
        print(f'Salary : {self.salary}')
    def annual_salary(self):
        print(f'Yearly Salary of {self.name} is : {self.salary*12}')
emp1=Employee('Raju','Assoicate Software Engineer',40000)
emp2=Employee('Ravi','CEO',90000)
emp1.display_info()
emp1.apply_raise(30)
emp1.annual_salary()
emp1.display_info()
print()
emp2.display_info()
emp2.apply_raise(30)
emp2.annual_salary()
emp2.display_info()