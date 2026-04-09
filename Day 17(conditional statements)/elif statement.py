# 1
ch=input("enter the character :")
if 'A' <=ch<='Z':
    print("The character is uppercase")
elif 'a'<=ch<='z':
    print("The character is lowercase")

# 2
num=int(input("enter the number :"))
if num%3==0 and num%5==0:
    print("Divisible by both")
elif num%5==0:
    print("Divisible by 5")
elif num%3==0:
    print("Divisible by 3")

# 3
ch=input("Enter the character :")
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    print("The character is alphabet")
elif '0'<=ch<='9':
    print("The character is digit")

# 4
ch=input("Enter the character :")
if 'A'<=ch<='Z':
    print("uppercase")
elif 'a'<=ch<='z':
    print("lowercase")
elif '0'<=ch<='9':
    print("digit")
else:
    print("symbol")