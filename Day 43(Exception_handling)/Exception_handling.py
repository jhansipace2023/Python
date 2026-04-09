# Single Exception Handling
# 1
try:
    a=45
    b=0
    result=a/b
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")

# 2
try:
    list=[10,20,30]
    print(list[4])
except IndexError:
    print("Index value out of range")

# 3
try:
    num=int("Python")
    print(num)
except ValueError:
    print("Invalid Conversion")

# Multiple Exception Handling
# 1
try:
    a=int(input("Enter the value of a :"))
    b=int(input("Enter the value of b :"))
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid User Input")

# 2
try:
    a=45
    b=2
    result=a//b
except ZeroDivisionError:
    print("Cannot divided by zero")
else:
    print(result)

# 3
try:
    a=45
    b=0
    print(a//b)
except ZeroDivisionError:
    print('Error')
finally:
    print("Program Completed")

# Raise Keyword
#1 WAP to withdraw money from  a bank account, raise exception if insufficient balance and min balance 1000 must be maintained
try:
    balance=5000
    withdraw=int(input('enter the amount to withdraw:'))

    if withdraw>balance:
        raise Exception('Insufficient balance')

    if balance-withdraw<1000:
        raise ValueError('minimum balance 1000 must be maintained in bank account')
except Exception as e:
    print('error:',e)
except ValueError as v:
    print('error:',v)

else:
    balance=balance-withdraw
    print(f'{withdraw} has been debited from account')
    print(f'after withdraw updated balance:{balance}')

finally:
    print('Thankyou for using ATM')

#2 WAP to perform banking operations such as Balance,deposite and withdraw using exception handling

balance=1000

def check_balance():
    print(f'your current balance is:{balance}')

def deposite(amount):
    global balance
    try:
        if amount<=0:
            raise ValueError("Deposite amount must be greater than zero")
        balance+=amount
        print(f'{amount} has been deposited successfully')
        print(f'after deposite updated balance is:{balance}')
    
    except ValueError as v:
        print('error',v)

def withdraw(amount):
    global balance
    try:
        if amount<=0:
            raise ValueError("withdrawal amount must be greater than zero")
        
        if amount>balance:
            raise Exception("Insufficient balance")
        
        balance-=amount
        print(f'{amount} has been credited')
        print(f'updated balance after withdraw:{balance}')

    except Exception as e:
        print('error:',e)

    except ValueError as v:
        print('error:',v)

while True:
    print("\n ----Bank Menu---")
    print("1. Check balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

    choice=input("enter your choice:")

    if choice=='1':
        check_balance()
    elif choice=='2':
        try:
            amt=float(input('enter amount to deposite:'))
            deposite(amt)
        except ValueError:
            print("Invalid input! Please enter a number:")
    
    elif choice=='3':
        try:
            amt=float(input('enter amount to withdraw:'))
            withdraw(amt)
        except ValueError:
            print("Invalid input! Please enter a number:")

    elif choice=='4':
        print("Thank you for using the banking system")
        break
    else:
        print("Invalid choice! Please try again")