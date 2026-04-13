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


# example 4 for multi Level inheritance   

# Base class: Account
class Account:
    def __init__(self, name, balance):
        """Initialize the account with name and balance."""
        self.name = name
        self.balance = balance  

    def display_info(self):
        """Display the account holder's name and balance."""
        print(f"Account holder: {self.name}")
        print(f"Balance: {self.balance}")

# Intermediate Class (Level 2) - Inheriting from Account
class BankAccount(Account):
    def __init__(self, name, balance):
        # Call the constructor of the Account class
        super().__init__(name, balance)

    def deposit(self, amount):
        """Deposit a specified amount into the bank account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw a specified amount from the bank account."""
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        self.balance -= amount
        print(f"{amount} withdrawn. New balance: {self.balance}")

# Derived Class (Level 3) - Inheriting from BankAccount
class SavingBankAccount(BankAccount):
    def __init__(self, name, balance):
        # Call the constructor of the BankAccount class
        super().__init__(name, balance)

    def withdraw(self, amount):
        """Override the withdraw method to apply a limit (max withdrawal of 10,000)."""
        if amount > 10000:
            raise ValueError("Max withdraw limit is 10,000.")
        super().withdraw(amount)  # Call the withdraw method of BankAccount class

# Creating instances
acc = Account('John Doe', 10000)  # Base class instance
print("Account Information:")
acc.display_info()

bank_acc = BankAccount('Jane Doe', 20000)  # Derived class instance (Level 2)
print("Bank Account Information:")
bank_acc.display_info()
bank_acc.deposit(5000)
bank_acc.withdraw(3000)

saving_acc = SavingBankAccount('Alice Smith', 30000)  # Derived class instance (Level 3)
print("Saving Account Information:")
saving_acc.display_info()
saving_acc.deposit(10000)
saving_acc.withdraw(9000)



# example 2 

# In multi-level inheritance : 
# In this type of inheritance, a new class is derived from a parent class which is derived from
# another parent class.
#  The new class or child class can inherit all the properties and method of
# both parent classes or existing class. 

#(Manager class that inherits properties from both an Employee class and a Person class. ) 
# Person → Employee → Manager
 
# Base class: Person (Level 1)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Intermediate class: Employee (Level 2) - Inherits from Person
class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Initialize the Person class (base class)
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        self.display_personal_info()
        print(f"Employee ID: {self.employee_id}") 

# Derived class: Manager (Level 3) - Inherits from Employee
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        # Initialize the Employee class (intermediate class)
        super().__init__(name, age, employee_id)
        self.department = department

    def display_manager_info(self):
        self.display_employee_info()
        print(f"Department: {self.department}")


# Create an instance of Manager (final class) 
m1 = Manager("King", 40, "M12345", "IT")
m1.display_manager_info()  




