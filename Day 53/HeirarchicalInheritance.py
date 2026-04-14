# 1
class vehicle:
    def start(self):
        print('Vehicle Starts')
class car(vehicle):
    def car_start(self):
        print('driving car')
class bike(vehicle):
    def bike_start(self):
        print('riding bike')
c=car()
b=bike()
c.start()
c.car_start()
b.start()
b.bike_start()

# 2
class employee:
    def work(self):
        print('Employee works')
class manager(employee):
    def manage(self):
        print("Manager manages the entire team")
class developer(employee):
    def code(self):
        print("Developer they write code")
class testing(employee):
    def test(self):
        print("They test applictions.")
m=manager()
d=developer()
m.work()
m.manage()
d.work()
d.code()
t=testing()
t.work()
t.test()

# 3
class BankAccount:   #Parent class
    def __init__(self,cname,acctno,balance):
        self.cname=cname
        self.acctno=acctno
        self.balance=balance
    def display(self):
        print(f'Customer name is : {self.cname}')
        print(f'Customer account number : {self.acctno}')
        print(f'Current balance is : {self.balance}')
        return self   #method chaining
    def deposit(self,amount):
        self.balance+=amount
        print(f'{amount} has been deposited')
        print(f'Updated balance is : {self.balance}')
        return self 
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f'{amount} has been withdrawn')
            print(f'Updated balance is :{self.balance}')
        else:
            print('Insufficient balance')
        return self
class SavingBankAccount(BankAccount):
    def __init__(self, /, cname, acctno, balance):
        super().__init__(cname, acctno, balance)
    def account_info(self):
        print('Saving Bank customer details')
        return self
class CurrentBankAccount(BankAccount):
    def __init__(self, /, cname, acctno, balance):
        super().__init__(cname, acctno, balance)
    def account_info(self):
        print('Current Bank customer details')
        return self
# Saving Bank Account
s1=SavingBankAccount('smith',1234,95000)
s1.account_info().display().deposit(1000).withdraw(500)
print()
# Current Bank Account
c1=CurrentBankAccount('Martin',9845,98000)
c1.account_info().display().deposit(2000).withdraw(1000)

# 4
class employee:
    def get_bonus(self,salary):
        self.salary=salary
        print(f'employee salary is : {self.salary}')
        print(f'employee bonus is : {self.salary * 0.10}')
class Developer(employee):
    def get_bonus(self, salary):
        self.salary=salary
        print(f'developer bonus is : {self.salary*0.30}')
class Manager(employee):
    def get_bonus(self, salary):
        self.salary=salary
        print(f'manager bonus is : {self.salary*0.50}')
d1=Developer()
m1=Manager()
d1.get_bonus(65000)
m1.get_bonus(75000)

# 5
class BankAccount:
    def __init__(self,cname,balance):
        self.cname=cname
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError('Amount should be greater than zero')
        self.balance+=amount
        print(f'{amount} deposited.Updated balance : {self.balance}')
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient balance")
        self.balance-=amount
        print(f'{amount} withdrawn.Updated balance : {self.balance}')
    def display(self):
        print(f'Account Holder : {self.cname}')
        print(f'Total balance : {self.balance}')
class SavingBankAccount(BankAccount):
    def __init__(self, cname, balance):
        super().__init__(cname, balance)
    def withdraw(self,amount):
        if amount>10000:
            raise ValueError('Max withdraw limit is 10000')
        super().withdraw(amount)
class SalaryAccount(BankAccount):
    def __init__(self, cname, balance,acctno):
        super().__init__(cname, balance)
        self.acctno=acctno
    def deposit(self,amount):
        if amount<20000:
            raise ValueError('Salary should be more than 20,000')
        super().deposit(amount)
c1=SavingBankAccount('smith',30000)
c2=SalaryAccount('Allen',40000,12345)
print('Saving Account Transactions')
try:
    c1.deposit(20000)
    c1.withdraw(30000)
    c1.display()
except ValueError as e:
    print("Error:",e)
print('Salary Account Transactions')
try:
    c2.deposit(2000)
    c2.withdraw(10000)
    c2.display()
except ValueError as e:
    print('Error :',e)