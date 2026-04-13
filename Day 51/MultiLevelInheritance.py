# Multi Level Inheritance
# 1
class student:
    def get_name(self):
        self.name=input("Enter the name:")
class marks(student):
    def get_mark(self):
        self.mark=int(input("Enter the mark:"))
class Result(marks):
    def display(self):
        print(f'Student name is : {self.name}')
        print(f'Student marks : {self.mark}')
        if self.mark>=35:
            print("Status:Pass")
        else:
            print("Status:Fail")
s1=Result()
s1.get_name()
s1.get_mark()
s1.display()

# 2
class Bank:
    def bank_name(self):
        self.bname='ICICI'
        print(f'Bank name : {self.bname}')
class Account(Bank):
    def __init__(self,cname,balance):
        self.cname=cname
        self.balance=balance
class transactions(Account):
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited')
        print(f'After deposit balance:{self.balance}')
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print(f'{amount} debited')
        print(f'After withdraw balance:{self.balance}')
    def display(self):
        print(f'Customer name is : {self.cname}')
        print(f'Bank balence is : {self.balance}')
s1=transactions('smith',98000)
s1.display()
s1.deposit(1000)
s1.withdraw(500)

# 3
class employee:
    def __init__(self,empno,ename,salary):
        self.empno=empno
        self.ename=ename
        self.salary=salary
    def display_employee(self):
        print(f'Employee number is : {self.empno}')
        print(f'Employee name is : {self.ename}')
        print(f'Employee salary is : {self.salary}')
class Department(employee):
    def __init__(self, empno, ename, salary,dname):
        super().__init__(empno, ename, salary)
        self.dname=dname
    def display_department(self):
        print(f'Department name is : {self.dname}')
class project(Department):
    def __init__(self, empno, ename, salary, dname,pid,project_name):
        super().__init__(empno, ename, salary, dname)
        self.pid=pid
        self.project_name=project_name
    def display(self):
        self.display_employee()
        self.display_department()
        print(f'Project id is : {self.pid}')
        print(f'Project name is : {self.project_name}')
p1=project(7819,'smith',98000,'research',12345,'department')
p1.display()