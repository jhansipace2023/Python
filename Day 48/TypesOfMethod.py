# Object method
class BankAccount:
    def __init__(self,cname,balance):
        self.came=cname
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'After deposit updated balance is:{self.balance}')
        else:
            print('Amount should be more than zero')
B1=BankAccount('allen',98000)
B1.deposit(1000)

# Class method
class BankAccount:
    bank_name='icici'
    def __init__(self,cname,balance):
        self.cname=cname
        self.balance=balance
    @classmethod
    def change_bank_name(cls,new_name):
        print(f'Before update bank name is:{BankAccount.bank_name}')
        cls.bank_name=new_name
        print(f'After update bank name is:{BankAccount.bank_name}')
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} has been deposited')
        print(f'After deposit updated balance is:{self.balance}')
    def display(self):
        print(f'Customer name is:{self.cname}')
        print(f'Initial balance is:{self.balance}')
B1=BankAccount('smith',45000)
B1.display()
B1.deposit(1000)
B1.change_bank_name('HDFC')

# Static method
class calculator:
    @staticmethod
    def addition(a,b):
        return a+b
print(calculator.addition(100,400))

# 1
class student:
    school_name='Qspiders'
    def __init__(self,sname,marks):
        self.sname=sname
        self.marks=marks
    def bonus_marks(self,extra_marks):
        self.marks=self.marks+extra_marks
        print(f'After bonus marks:{self.marks}')
    @classmethod
    def change_school_name(cls,new_name):
        cls.school_name=new_name
        print(f'New school name is:{student.school_name}')
    @staticmethod
    def check_marks(marks):
        return marks>=35
    def display(self):
        print(f'Student name is:{self.sname}')
        print(f'Initial marks are:{self.marks}')
        if student.check_marks(self.marks):
            print(f'{self.sname} is pass')
        else:
            print(f'{self.sname} is fail')
s1=student('smith',40)
s1.display()
s1.bonus_marks(10)
s1.change_school_name('Pyspiders')
