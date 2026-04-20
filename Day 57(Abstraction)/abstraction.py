# Abstraction
# example 1
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print('Car starts with key')
obj=car()
obj.start()

# 1
class Bank(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class ICICI(Bank):
    def __init__(self,balance):
        self.balance=balance
        print(f'Initial bank balance is : {self.balance}')
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'{amount} has been deposited')
            print(f'After deposit balance : {self.balance}')
        else:
            print(f'Amount should be greater than zero')
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f'{amount} has been debited')
            print(f'After withdraw balance : {self.balance}')
        else:
            print('Insufficient balance')
    def check_balance(self):
        print(f'Bank balance : {self.balance}')
I=ICICI(98000)
I.deposit(1000)
I.withdraw(500)
I.check_balance()

# 1 - Combination of all pillars
from abc import ABC,abstractmethod
# Abstraction
class BankAccount(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
# Inheritance + Encapsulation
class CustomerAccount(BankAccount):
    def __init__(self,name,acc_no,balance=0):
        self.__name=name
        self.__acc_no=acc_no
        self.__balance=balance
    # Getter method
    def get_name(self):
        return self.__name
    def get_acc_no(self):
        return self.__acc_no
    def get_balance(self):
        return self.__balance
    # Setter with validation
    def set_name(self,name):
        if name.isalpha():
            self.__name=name
        else:
            print('Invalid name! Only alphabets allowed')
    # Polymorphism
    def deposit(self, amount):
        if amount<=0:
            print('Deposit amount must be positive')
        else:
            self.__balance+=amount
            print(f'{amount} deposited successfully')
    def withdraw(self,amount):
        if amount<=0:
            print('Withdrawal amount must be positive')
        elif amount>self.__balance:
            print('Insufficient balance')
        else:
            self.__balance-=amount
            print(f'{amount} withdraw successfull')
    def check_balance(self):
        print(f'Current balance : {self.__balance}')
# Validation functions
def validate_name(name):
    return name.isalpha()
def validate_account_number(acc_no):
    return acc_no.isdigit() and len(acc_no)==6
# Main Program
def main():
    print('=====Bank System=====')
    # name validation
    while True:
        name=input('Enter customer name:')
        if validate_name(name):
            break
        print('Invalid name! Use only alphabets')
    # account number validation
    while True:
        acc_no=input('Enter 6-digit account number')
        if validate_account_number(acc_no):
            break
        print('Invalid account number! Must be 6 digits')
    customer=CustomerAccount(name,acc_no)
    # Menu
    while True:
        print('\n1.Deposit')
        print('2.Withdraw')
        print('3.Check balance')
        print('4.Exit')
        choice=input('Enter your choice : ')
        if choice=='1':
            try:
                amount=float(input('Enter deposit amount:'))
                customer.deposit(amount)
            except ValueError:
                print('Invalid amount')
        elif choice=='2':
            try:
                amount=float(input('Enter withdrawal amount'))
                customer.withdraw(amount)
            except ValueError:
                print('Invalid amount')
        elif choice=='3':
            customer.check_balance()
        elif choice=='4':
            print('Thank you for using the system')
            break
        else:
            print('Invalid choice')
# Run Program
main()