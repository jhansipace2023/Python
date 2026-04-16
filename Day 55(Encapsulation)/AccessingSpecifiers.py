# Public Access modifiers
# example
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    # accessing public variables inside class
    def display(self):
        print(f'Customer name : {self.name}')
        print(f'Bank balance : {self.balance}')
obj=Bank('smith',87000)
obj.display()
print()
print(f'Customer name accessing outside class : {obj.name}')
print(f'Bank balance accessing outside class : {obj.balance}')
# modifying public variable
obj.name='Allen'
obj.balance=98000
print(f'after updating vale name : {obj.name}')
print(f'after updating value balance : {obj.balance}')

# Protected Access modifiers
# example
class Bank:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance
    # accessing protected variables inside class
    def display(self):
        print(f'Customer name : {self._name}')
        print(f'Bank balance : {self._balance}')
obj=Bank('smith',87000)
obj.display()

# example 2 using protected method
class Bank:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance
    def _showdetails(self):
        print(f'Customer name : {self._name}')
        print(f'Bank balance : {self._balance}')
class customer(Bank):
    def display(self):
        self._showdetails()
obj=customer('smith',98000)
obj.display()

# Private Access Modifiers
class Bank:
    def __init__(self,name,balance):
        self._name=name          # protected variable
        self.__balance=balance   # private variable
    def _showdetails(self):
        print(f'Customer name : {self._name}')
        print(f'Bank balance : {self.__balance}')
class customer(Bank):
    def display(self):
        self._showdetails()
obj=customer('smith',98000)
obj.display()
# accessing private variable outside the class
# print(obj.__balance)
# accessing private variable outside the class using Name Mangling
print(obj._Bank__balance)

# ex using getter & setter methods
class employee:
    def __init__(self,empno,ename,salary):
        self.empno=empno
        self.ename=ename
        self.__salary=salary      # private variable
    # Getter method
    def get_salary(self):
        return self.__salary
    # Setter method
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
        else:
            print('Salary should be more than zero')
e=employee(7839,'smith',800)
print(f'Employee no : {e.empno}')
print(f'Employee name : {e.ename}')
# accessing private variable using getter method
print(f'Employee salary : {e.get_salary()}')
# updating private variable using setter
e.set_salary(98000)
print(f'Updated salary is : {e.get_salary()}')

# Example using @ decorator to define getter and setter
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance        # private attribute
    @property
    def balance(self):
        return self.__balance         # getter to access the balance value
    @balance.setter
    def balance(self,new):
        if isinstance(new,int):       # Ensuring new balance is an integer
            self.__balance=new
        else:
            raise ValueError('Invalid formatted data')   # Raise error if its not an integer
# create an instance of BankAccount
c1=BankAccount(3000)
# Update the balance using the setter
c1.balance=45000     
# Print the updated balance using the getter
print(c1.balance)