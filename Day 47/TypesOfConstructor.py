# 1
class employee:
    def read(self,ename='smith',salary=98000):
        self.ename=ename
        self.salary=salary
emp1=employee()
emp1.read()
print(f'Employee name is : {emp1.ename} and salary is : {emp1.salary}')
emp2=employee()
emp2.read('allen',75000)
print(f'Employee name is : {emp2.ename} and salary is : {emp2.salary}')

# Example for parameterized constructor
class employee:
    def __init__(self,ename,job):
        self.ename=ename
        self.job=job
    def display(self):
        print(f'Employee name is : {self.ename}')
        print(f'Designation is : {self.job}')
e1=employee('smith','analyst')
e1.display()
print()
e2=employee('allen','salesman')
e2.display()

# Example for non-parameterized constructor
class employee:
    def __init__(self):
        pass
    def display(self):
        print(f'Employee name is : {self.ename}')
        print(f'Department number is : {self.deptno}')
e1=employee()
e1.ename='smith'
e1.deptno=10
e1.display()

# Example for Default constructor
class trainer:
    def read(self,tname='Ram',sal='98000'):
        self.tname=tname
        self.sal=sal
t1=trainer()
t1.read()
print(f'Trainer name is : {t1.tname} and salary is : {t1.sal}')

t2=trainer()
t2.read('Chandhana',50000)
print(f'Trainer name is : {t2.tname} and salary is : {t2.sal}')

# Example for Parameterized constructor
class trainer:
    def __init__(self,tname,course):
        self.tname=tname
        self.course=course
    def display(self):
        print(f'Trainer name is: {self.tname}')
        print(f'Course name is : {self.course}')
t1=trainer('Ram','Python')
t1.display()

# Example for Non-Parameterized constructor
class trainer:
    def __init__(self):
        pass
    def display(self):
        print(f'Trainer name is : {self.tname}')
        print(f'Course name is : {self.course}')
t1=trainer()
t1.tname='Ram'
t1.course='Python'
t1.display()

# Example for declaring instance variables
class Employee:
    def __init__(self,ename,job):
        self.ename=ename      # instance variables
        self.job=job          # instance variables
    def display(self):
        print(f'Employee name is : {self.ename}, job : {self.job}')
emp1=Employee('smith','SQL Developer')
emp2=Employee('scott','Python Developer')
emp1.display()
emp2.display()

# Example for declaring static variables
class Employee:
    company_name='TechCorp'          # Static variables
    def __init__(self,ename,job):
        self.ename=ename
        self.job=job
    def display(self):
        print(f'Name : {self.ename} , Job : {self.job} and Company : {Employee.company_name}')
emp1=Employee('smith','SQL Developer')
emp2=Employee('scott','Python Developer')
emp1.display()
emp2.display()

# Local Variables
class Employee:
    def __init__(self,ename,monthly_salary,job):
        self.ename=ename
        self.monthly_salary=monthly_salary
        self.job=job
    def calculate_annual_salary(self):
        annual_salary=self.monthly_salary*12
        print(f'Employee : {self.ename}, job : {self.job}')
        print(f'Annual salary : {annual_salary}')
emp=Employee('smith',5000,'SQL Developer')
emp.calculate_annual_salary()