# # Hybrid Inheritance
# # 1
# class A:
#     def display_A(self):
#         print('Class A')
# class B(A):
#     def display_B(self):
#         print('Class B')
# class C(A):
#     def display_C(self):
#         print('Class C')
# class D(B,C):
#     def display_D(self):
#         print('Class D')
# obj=D()
# obj.display_A()
# obj.display_B()
# obj.display_C()
# obj.display_D()

# # 2
# class A:
#     def __init__(self):
#         print("Constructor A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('Constructor B')
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('Constructor C')
# class D(B,C):
#     def __init__(self):
#         super().__init__()
#         print('Constructor D')
# obj=D()
# print(D.__mro__)

# # 3
# class Account:
#     def __init__(self,acc_holder,balance):
#         self.acc_holder=acc_holder
#         self.balance=balance
#     def show_balance(self):
#         print(f'account holder : {self.acc_holder}')
#         print(f'Balance : {self.balance}')
# class savings(Account):         # single level inheritance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print(f'Deposited : {amount}')
# class current(Account):         # heirarchical inheritance
#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#         print(f'Withdraw : {amount}')
# class combineAccount(savings,current):      # multiple Inheritance
#     pass
# acct=combineAccount('smith',98000)
# acct.show_balance()
# acct.deposit(1000)
# acct.withdraw(500)
# acct.show_balance()

# # 4
# class Animals:
#     def __init__(self):
#         pass
#     def display(self):
#         print('Welcome to animal kingdom')
#         return self
# class cat(Animals):
#     def __init__(self):
#         super().__init__()
#     def display_A(self):
#         print('I am cat')
#         return self
# class dog(cat):
#     def __init__(self):
#         super().__init__()
#     def display_B(self):
#         print('I am dog')
#         return self
# class cow(Animals):
#     def __init__(self):
#         super().__init__()
#     def display_C(self):
#         print('I am cow')
#         return self
# class horse(cat,cow,dog):
#     def __init__(self):
#         super().__init__()
#     def display_D(self):
#         print('I am horse')
#         return self
# obj=horse()
# obj.display().display_A().display_C().display_D()


# 5
# Base Account
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print(f'BankAccount created for : {self.name}')
    def display(self):
        print(f'Account Holder : {self.name}')
        print(f'Balance : {self.balance}')
        return self
# single inheritance
class SavingsAccount(BankAccount):
    def __init__(self, name, balance,interest):
        super().__init__(name, balance)
        self.interest=interest
        print(f'SavingsAccount created for : {self.name}')
    def display_savings(self):
        print(f'Interest Rate : {self.interest}%')
        return self
# multilevel inheritance
class PremiumSavings(SavingsAccount):
    def __init__(self, name, balance, interest,bonus):
        super().__init__(name, balance, interest)
        self.bonus=bonus
        print(f'PremiumSavings created for {self.name}')
    def display_premium(self):
        print(f'Bonus : {self.bonus}')
        return self
# multiple inheritance
class Loan:
    def __init__(self,loan_amount):
        self.loan_amount=loan_amount
        print(f'Loan approved : {self.loan_amount}')
    def display_loan(self):
        print(f'Loan Amount : {self.loan_amount}')
        return self
class CustomerAccount(PremiumSavings,Loan):
    def __init__(self, name, balance, interest, bonus,loan_amount):
        PremiumSavings.__init__(self,name, balance, interest, bonus)
        Loan.__init__(self,loan_amount)
        print(f'CustomerAccount created for : {self.name}')
    def display_customer(self):
        print(f'Complete details of : {self.name}')
        return self
# Heirarchical inheritance
class CurrentAccount(BankAccount):
    def __init__(self, name, balance,overdraft):
        super().__init__(name, balance)
        self.overdraft=overdraft
        print(f'CurrentAccount created for : {self.name}')
    def display_current(self):
        print(f'Overdraft Linit : {self.overdraft}')
        return self
# Main Program
print('\n Single Inheritance(savings)')
s=SavingsAccount('smith',1000,5)
s.display().display_savings()
print(f'\nMultiple Inheritance (Premium Savings)')
p=PremiumSavings('scott',15000,6,500)
p.display().display_savings().display_premium()
print(f'\nMultiple Inheritance (Customer Account + loan)')
c=CustomerAccount('Martin',20000,7,1000,50000)
c.display().display_savings().display_premium().display_loan().display_customer()
print('\nHeirarchical Inheritance (current Account)')
ca=CurrentAccount('king',25000,10000)
ca.display().display_current()