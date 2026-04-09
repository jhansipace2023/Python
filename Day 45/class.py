# 5
class employee:
    # class variables
    company_name='pyspiders'
    location='basavangudi'
e1=employee()
# Object variables
e1.ename='smith'
e1.sal=98000
e1.job='analyst'
print(f'Employee name:{e1.ename},sal:{e1.sal},job:{e1.job} and company name:{employee.company_name} and location is :{employee.location}')

# 6
class employee:
    ename='smith'
    sal=45000
    deptno=10

    def display():
        print(f'Employee name is : {employee.ename}')
        print(f'Employee salary is : {employee.sal} and deptno is : {employee.deptno}')
employee.display()

# 7
class student:
    sname='martin'
    age=26

    def display(self):
        print(f'Student name is : {s1.sname}')
        print(f'Student age is : {s1.age}')
s1=student()
s1.display()

# OR
class student:
    sname='martin'
    age=26

    def display():
        print(f'Student name is : {s1.sname}')
        print(f'Student age is : {s1.age}')
s1=student()
student.display()

# 8
class employee:
    ename='smith'
    salary=45000

    def display(self):
        print(f'Employee name : {self.ename}')
        print(f'Employee monthly salary : {self.salary}')
        print(f'Employee annual salary : {self.salary*12}')
e1=employee()
e1.display()

# Example using function as object
class employee:
    dname='research'
    def details(self,ename,sal):
        self.ename=ename
        self.sal=sal
    def display(self):
        print(f'Employee name:{self.ename}')
        print(f'Employee department name:{self.dname}')
        print(f'Employee salary is:{self.sal}')
e1=employee()
e1.details('scott',98000)
e1.display()
print()
e2=employee()
e2.details('King',50000)
e2.display()

# 9
class Bank:
    bankname='icici'

    def details(self,cname,balance):
        self.cname=cname
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'After deposit updated balance:{self.balance}')
        else:
            print('Amount should be greater than zero')
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} has been debited')
            print(f'After withdraw updated balance:{self.balance}')
        else:
            print("Insufficeint Balance")
    def display(self):
        print(f'Customer name:{self.cname}')
        print(f'Initial bank balance is:{self.balance}')
c1=Bank()
c1.details('smith',98000)
c1.display()
c1.deposit(1000)
c1.withdraw(500)
c2=Bank()
c2.details('King',50000)
c2.display()
c2.deposit(1000)
c2.withdraw(500)


# 10
class employee:
    company_name='pyspiders'

    def details(self,ename,sal):
        self.ename=ename
        self.sal=sal

    def addSal(self,amount):
        if amount>0:
            self.sal=self.sal+amount
            print(f'Present Salary : {self.sal}')
        else:
            print("Amount should be greater than zero")
    
    def display(self):
        print(f'Employee name : {self.ename} and sal : {self.sal}')
e1=employee()
e1.details('smith',98000)
e1.display()
e1.addSal(1000)
