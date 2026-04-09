# 1
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print(f'Customer name is : {self.name}')
        print(f'Initial bank balance is : {self.balance}')
class SavingAccount(Bank):
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'After deposit updated balance is : {self.balance}')
        else:
            print('Amount should be more than zero')
s1=SavingAccount('smith',98000)
s1.display()
s1.deposit(1000)

# 2
class student:
    def __init__(self,name,subject,marks):
        self.name=name
        self.subject=subject
        self.marks=marks
    def display(self):
        print(f'Student name is : {self.name}')
        print(f'Student subject is : {self.subject} and marks are : {self.marks}')
class result(student):
    def check_marks(self):
        if self.marks>=35:
            print("Result:Pass")
        else:
            print("Result:Fail")
c1=result('smith','sql',40)
c1.display()
c1.check_marks()

# 3
class employee:
    def __init__(self,ename,salary):
        self.ename=ename
        self.salary=salary
    def display_emp(self):
        print(f'Employee name is : {self.ename} and salary is : {self.salary}')
class designation(employee):
    def employee_designation(self,job):
        self.job=job
    def display_job(self):
        print(f'Employee designation : {self.job}')
obj=designation('smith',45000)
obj.employee_designation('analyst')
obj.display_emp()
obj.display_job()

# 4
class Bank:
    def __init__(self,acctno,balance):
        self.acctno=acctno
        self.balance=balance
    def account_details(self):
        print(f'Account Number : {self.acctno}')
        print(f'Balance : {self.balance}')
class SavingAccount(Bank):
    def deposit(self,amount):
        try:
            if amount<=0:
                raise ValueError("Deposit amount must be positive")
            self.balance+=amount
            print(f'Deposited Amount:{amount}')
        except ValueError as e:
            print("Deposit Error :",e)
    def withdraw(self,amount):
        try:
            if amount<=0:
                raise ValueError("Withdrawal amount must be positive")
            if amount>self.balance:
                raise ValueError("Insufficient balance")
            self.balance-=amount
            print(f'Withdrawn Amount : {amount}')
        except ValueError as e:
            print("Withdrawal Error :",e)
    def updated(self):
        print(f"Updated Balance : {self.balance}")
# creating child object
b=SavingAccount(12345,50000)
b.account_details()
b.deposit(15000)
b.withdraw(2000)
b.updated()

# 5
# Parent class
class Ticket:
    def set_ticket_details(self,name,ticket_no):
        self.name=name
        self.ticket_no=ticket_no
    def show_ticket_details(self):
        print("Passenger Name :",self.name)
        print("Ticket Number :",self.ticket_no)
# child class
class FlightTicket(Ticket):
    def set_flight_details(self,flight_name,seat_no):
        self.flight_name=flight_name
        self.seat_no=seat_no
    def show_flight_details(self):
        print("Flight Name:",self.flight_name)
        print("Seat number:",self.seat_no)
# creating object
obj=FlightTicket()
#Taking input
name=input("Enter passenger name:")
ticket_no=input("Enter ticket number:")
flight_name=input("Enter flight name:")
seat_no=input("Enter seat number:")
# setting values
obj.set_ticket_details(name,ticket_no)
obj.set_flight_details(flight_name,seat_no)
# Display output
obj.show_ticket_details()
obj.show_flight_details()