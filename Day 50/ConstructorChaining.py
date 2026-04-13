# Example 1:without using super keyword
class parent:
    def __init__(self):
        print("This is a parent class")
class child(parent):
    def __init__(self):
        print("This is a child class")
obj=child()

# Ex 2 using super keyword
class parent:
    def __init__(self):
        print("This is a parent class")
class child(parent):
    def __init__(self):
        super().__init__()
        print("This is a child class")
obj=child()

# 1
class college:
    def __init__(self,sname,age):
        self.sname=sname
        self.age=age
class student(college):
    def __init__(self, sname, age,subject):
        super().__init__(sname, age)
        self.subject=subject
    def display(self):
        print(f'Student name is:{self.sname}')
        print(f'Age : {self.age}')
        print(f'Subject : {self.subject}')
s1=student('smith',26,'python')
s1.display()

# 2
class Bank:
    def __init__(self,bankname,name):
        self.bankname=bankname
        self.name=name
    def details(self):
        print(f"Bankname is : {self.bankname}")
        print(f"Customer name is : {self.name}")
class Account(Bank):
    def __init__(self, bankname, name,balance,acctno):
        super().__init__(bankname, name)
        self.balance=balance
        self.acctno=acctno
    def display(self):
        print(f'Account number : {self.acctno}')
        print(f'Initial balance is : {self.balance}')
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'After deposit updated balance : {self.balance}')
        else:
            print("Amount should be more than zero")
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} has been debited')
            print(f'After withdraw updated balance is : {self.balance}')
        else:
            print("Insufficient balance")
obj=Account('ICICI','smith',98000,12345)
obj.details()
obj.display()
obj.deposit(1000)
obj.withdraw(800)

# 3
class employee:
    def __init__(self,empno,ename):
        self.empno=empno
        self.ename=ename
class employeedetails(employee):
    def __init__(self, empno, ename,salary,job):
        super().__init__(empno, ename)
        self.salary=salary
        self.job=job
    def display(self):
        print(f'Employee number is : {self.empno}, name is : {self.ename}, salary is : {self.salary} and designation is : {self.job}')
e1=employeedetails(7839,'smith',98000,'analyst')
e1.display()

# Method Chaining in Python
# Ex 1
class Bank:
    def __init__(self,bankname,name):
        self.bankname=bankname
        self.name=name
    def details(self):
        print(f'Bankname is : {self.bankname}')
        print(f'Customer name : {self.name}')
        return self
class Account(Bank):
    def __init__(self, bankname, name,balance,acctno):
        super().__init__(bankname, name)
        self.balance=balance
        self.acctno=acctno
    def display(self):
        print(f'Account number : {self.acctno}')
        print(f'Initial balance is : {self.balance}')
        return self
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'After deposit updated balance : {self.balance}')
        else:
            print("Amount should be more than zero")
        return self
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} has been debited')
            print(f'After withdraw updated balance is : {self.balance}')
        else:
            print("Insufficient balance")
        return self
obj=Account('ICICI','smith',98000,12345)
obj.details().display().deposit(1000).withdraw(500)

# 1
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount must be grater than zero")
        self.balance+=amount
        print(f'{amount} deposited.New balance : {self.balance}')
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient funds")
        if amount<=0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        self.balance-=amount
        print(f'{amount} withdrawn.New balance:{self.balance}')
class SavingBankAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    def withdraw(self, amount):
        if amount>10000:
            raise ValueError("Max withdraw limit is 10,000")
        super().withdraw(amount)
c1=BankAccount("Steve",50000)
c2=SavingBankAccount('Alice',30000)
c1.deposit(10000)
c1.withdraw(20000)
try:
    c1.deposit(5000)
    c2.withdraw(15000)
except ValueError as e:
    print(e)
c2.withdraw(10000)