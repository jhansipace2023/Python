# 1
print("---ATM MENU---")
print("1.Check Balance")
print("2.Deposit Money")
print("3.Withdraw Money")
choice=int(input("Enter the 1 or 2 0r 3:"))
balance=5000
if choice==1:
    print(f'Account Balance is;{balance}')
elif choice==2:
    deposit=int(input("Enter the amount to deposit"))
    balance=balance+deposit
    print(f'{deposit} has been deposited to account')
elif choice==3:
    withdraw=int(input("Enter the amount"))
    balance=balance-withdraw
    print(f'after withdraw pending bank balance is:{balance}')
else:
    print('invalid choice')

# 2
print("Welcome to Book My Show!")
theater_name = input("Enter the name of the theater (PVR, Inox):")

if theater_name == "PVR":
    print("In movies available at PVR:")
    movie1 = "Avatar: The Way of Water - RS 855"
    movie2 = "The Batman - RS 800"
    ticket_price1 = 855
    ticket_price2 = 800

    print(f"1. {movie1}")
    print(f"2. {movie2}")

    movie_choice = input("Enter the number to select movie (1 or 2):")

    if movie_choice == "1":
        selected_movie = movie1
        ticket_price = ticket_price1
    elif movie_choice == "2":
        selected_movie = movie2
        ticket_price = ticket_price2
    else:
        print("Invalid choice")

elif theater_name == "Inox":
    print("In movies available at Inox:")
    movie1 = "Mission: Impossible - Fallout - RS 900"
    movie2 = "Jurassic World: Dominion - RS 950"
    ticket_price1 = 900
    ticket_price2 = 950

    print(f"1. {movie1}")
    print(f"2. {movie2}")

    movie_choice = input("Enter the number to select movie (1 or 2):")

    if movie_choice == "1":
        selected_movie = movie1
        ticket_price = ticket_price1
    elif movie_choice == "2":
        selected_movie = movie2
        ticket_price = ticket_price2
    else:
        print("Invalid choice")

else:
    print("Sorry, the theater name is not available")

# 3
print("=== Simple Calculator ===")
print("select operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = input('enter choice (1/2/3/4):')
num1 = float(input('enter the first number:'))
num2 = float(input('enter the second number:'))

if choice == '1':
    print(f'the result of addition: {num1 + num2}')
elif choice == '2':
    print(f'the result of subtraction: {num1 - num2}')
elif choice == '3':
    print(f'the result of multiplication: {num1 * num2}')
elif choice == '4':
    print(f'the result of division: {num1 / num2}')
else:
    print('Invalid choice')

# 4
score = int(input("Enter the student's score (0-100):"))

if 90 <= score <= 100:
    print("grade: A")
elif 80 <= score < 90:
    print("grade: B")
elif 70 <= score < 80:
    print("grade: C")
elif 60 <= score < 70:
    print("grade: D")
elif 0 <= score < 60:
    print("grade: F")
else:
    print("Invalid score")

# 5
a, b, c = 56, 34, 89

if a > b and a > c:
    if b > c:
        print(f'{b} is the second greatest number')
    else:
        print(f'{c} is the second greatest number')
elif b > a and b > c:
    if a > c:
        print(f'{a} is the second greatest number')
    else:
        print(f'{c} is the second greatest number')
else:
    if a > b:
        print(f'{a} is the second greatest number')
    else:
        print(f'{b} is the second greatest number')

# 6
n = int(input('enter a year'))

if (n % 4 == 0) and (n % 400 == 0 or n % 100 != 0):
    print('given year is leap year')
    if n % 2 == 0:
        print('number is even')
    else:
        print('odd')
else:
    print('it is not a leap year')