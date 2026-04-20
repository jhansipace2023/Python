# Method Overloading
# example 1
class Demo:
    def add(self,*args):
        return sum(args)
obj=Demo()
print(obj.add(10,20))
print(obj.add(11,33,45))
print(obj.add(87,45,56,98,56))

# Example 2
class Demo:
    def add(self,*args):
        result=0
        for i in args:
            result=result+i
        return result
obj=Demo()
print(obj.add(10,20))
print(obj.add(11,33,45))
print(obj.add(87,45,56,98,56))

# example 3
class Demo:
    def add(self,*args):
        result=1
        for i in args:
            result=result*i
        return result
obj=Demo()
print(obj.add(1,2))
print(obj.add(1,3,4))
print(obj.add(8,4,5,9,5))

# Method Overriding
# example 1
class parent:
    def display(self):
        print('This is parent class')
class child(parent):
    def display(self):
        print('This is child class')
obj=child()
obj.display()

# example 2 Using super keyword
class parent:
    def display(self):
        print('This is parent class')
class child(parent):
    def display(self):
        super().display()
        print('This is child class')
obj=child()
obj.display()

# 1
class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f'{amount} has been deposited')
        print(f'After deposit updated balance : {self.balance}')
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient Bank balance')
        elif amount<self.balance:
            self.balance-=amount
            print(f'{amount} has been debited from account')
            print(f'After withdraw updated bank balance : {self.balance}')
    def check_balance(self):
        print(f'Initial bank balance is : {self.balance}')
# subclass with overriding
class savingAccount(BankAccount):
    # Overrriding withdraw method
    def withdraw(self,amount):
        if amount>10000:
            print('Limit exceeded! Max withdrawal is 10000')
        else:
            super().withdraw(amount)
# objects
acc1=BankAccount('smith',98000)
acc2=savingAccount('allen',97000)
# operations
acc1.check_balance()
acc1.deposit(2000)
acc1.withdraw(5000)
print()
acc2.check_balance()
acc2.deposit(3000)
acc2.withdraw(15000)
acc2.withdraw(8000)

# 2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calculate_salary(self,bonus):
        return self.salary+bonus
    def display_employee(self,bonus):
        print(f'Employee name is : {self.name}')
        print(f'Salary before bonus : {self.salary}')
        print(f'Salary after bonus : {self.calculate_salary(bonus)}')
class Manager(Employee):
    def calculate_salary(self, bonus):
        return self.salary+bonus
    def display_manager(self,bonus):
        print(f'Manager name is : {self.name}')
        print(f'Salary before bonus : {self.salary}')
        print(f'Salary after bonus : {self.calculate_salary(bonus)}')
# objects
e1=Employee('smith',30000)
m1=Manager('scott',50000)
# display details with custom bonuses
print('Employee details')
e1.display_employee(5000)    # emp bonus passed as 5000
print()
print('Manager details')
m1.display_manager(10000)     # Manager uses default bonus 10000

