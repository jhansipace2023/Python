# Example
class father:
    def show_father_details(self):
        print(f'This class belongs to first parent')
class mother:
    def show_mother_details(self):
        print(f'This class belongs to second parent')
class child(mother,father):
    def show_child_details(Self):
        print(f'This class belongs to child')
c1=child()
c1.show_child_details()
c1.show_father_details()
c1.show_mother_details()

# 1 Same method name in multiple classes
class A:
    def display(self):
        print('Class A')
class B:
    def display(self):
        print('Class B')
class C(B,A):
    def display(self):
        print('Class C')
obj=C()
obj.display()
print(C.__mro__)

# Ex 2 using classname.methodname to achieve parent class property
class A:
    def display(self):
        print('class A')
class B:
    def display(self):
        print('class B')
class C(B,A):
    def display(self):
        B.display(self)
        A.display(self)
obj=C()
obj.display()
print(C.__mro__)

# 2
class A:
    def __init__(self):
        super().__init__()
        print('class A')
class B:
    def __init__(self):
        super().__init__()
        print('class B')
class C(B,A):
    def __init__(self):
        super().__init__()
        print('class C')
obj=C()


# 3
class checkBalance:
    def show_balance(self):
        print(f'Current balance : {self.balance}')
class Deposit:
    def deposit_amount(self,amount):
        if amount<=0:
            print("Invalid deposit amount! Amount must be graeter than 0.")
        else:
            self.balance+=amount
            print(f'Deposited Amount:{amount}')
            print(f'Updated Balance after deposit : {self.balance}')
class withdraw:
    def withdraw_amount(self,amount):
        if amount<=0:
            print("Invalid withdrawal amount!Amount must be greater than 0.")
        elif amount>self.balance:
            print("Insufficient balance! Withdrawal failed.")
        else:
            self.balance-=amount
            print(f'Withdrawn amount:{amount}')
            print(f'Updated Blance after withdrawal : {self.balance}')
class Bank(checkBalance,Deposit,withdraw):
    def __init__(self,cname,acctno,balance):
        self.cname=cname
        self.acctno=acctno
        self.balance=balance
    def display_details(self):
        print(f'Customer name : {self.cname}')
        print(f'Account Number : {self.acctno}')
        print(f'Opening Balance : {self.balance}')
customer=Bank('smith',1234,98000)
customer.display_details()
customer.show_balance()
customer.deposit_amount(2000)
customer.withdraw_amount(3000)
print(Bank.mro())

# 4
class PersonalDetails:
    def set_name(self,name):
        self.name=name
    def show_name(self):
        print('Name:',self.name)
class JobDetails:
    def set_salary(self,salary):
        self.salary=salary
    def show_salary(self):
        print("Salary:",self.salary)
class Employee(PersonalDetails,JobDetails):
    def show_details(self):
        self.show_name()
        self.show_salary()
e=Employee()
e.set_name('smith')
e.set_salary(50000)
e.show_details()

# 5
class BankDetails:
    def set_bank(self,bank_name):
        self.bank_name=bank_name
    def show_bank(self):
        print("Bank Name : ",self.bank_name)
class AccountDetails:
    def set_balance(self,balance):
        self.balance=balance
    def show_balance(self):
        print("Balance :",self.balance)
class Customer(BankDetails,AccountDetails):
    def deposit(self,amount):
        self.balance+=amount
        print("After deposit:",self.balance)
    def withdraw(self,amount):
        self.balance==amount
        print("After withdraw:",self.balance)
    def show_details(self):
        self.show_bank()
        self.show_balance()
obj=Customer()
obj.set_bank("SBI")
obj.set_balance(5000)
obj.show_details()
obj.deposit(2000)
obj.withdraw(1000)