# 1
day=eval(input("Enter the number:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Number")

# # 2
operation=eval(input("Enter the number:"))
num1=9
num2=2
match operation:
    case 1:
        print(f'Sum of {num1} and {num2}:{num1+num2}') 
    case 2:
        print(f'Difference of {num1} and {num2}:{num1-num2}')
    case 3:
        print(f'Product of {num1} and {num2}:{num1*num2}')
    case 4:
        if num2!=0:
            print(f'True division:{num1/num2}')
        else:
            print('ZeroDivision Error')  
    case 5:
        if num2!=0:
            print(f'Floor Division:{num1//num2}')
        else:
            print('ZeroDivision Error')
    case 6:
        print(f'Exponent is:{num1**num2}')
    case 7:
        print(f'Modulus is:{num1%num2}')
    case _:
        print('Invalid Operation')  

# 3
balance=97000
while True:
    print("\n---ATM Menu---")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice=eval(input("Enter your choice(1-4):"))
    match choice:
        case 1:
            print(f'Your balance is:Rs{balance}')
        case 2:
            amount=float(input("Enter amount to deposit:"))
            if amount>0:
                balance=balance+amount
                print(f'Rs{amount} deposited successfully')
                print(f'Updated balance:Rs{balance}')
            else:
                print('Inavlid amount')
        case 3:
            amount=float(input("Enter amount to withdraw:"))
            if amount<=balance and amount>0:
                balance=balance-amount
                print(f'Rs{amount} withdraw successful')
                print(f'Updated balance:Rs{balance}')
            else:
                print("Insufficient balance")
        case 4:
            print("Thank You for using ATM! Bye")

# 4
num=eval(input("Enter the number:"))
while True:
    print("1.Palindrome")
    print("2.Armstrong Number")
    print("3.Strong Number")
    print("4.Exit")
    choice=eval(input("Enter your choice:"))
    match choice:
        case 1:
            temp=num
            rev=0
            while num>0:
                digit=num%10
                rev=rev*10+digit
                num=num//10
            if temp==rev:
                print(f'{temp} is Palindrome')
            else:
                print(f'{temp} is not Palindrome')
        case 2:
            temp=num
            sum_cubes=num*num
            length=len(str(num))
            while num>0:
                digit=num%10
                sum_cubes=sum_cubes+digit**length
                num=num//10
            if temp==sum_cubes:
                print(f'{temp} is Armstrong number')
            else:
                print(f'{temp} is not armstrong number')
        case 3:
            temp=num
            sum=0
            while num>0:
                digit=num%10
                fact=1
                i=1
                while i<=digit:
                    fact=fact*i
                    i=i+1
                sum=sum+fact
                num=num//10
            if sum==temp:
                print("Strong number")
            else:
                print("Not strong number")
        case 4:
            print("Exit")
        case _:
            print("invalid choice")

