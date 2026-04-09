num=int(input("enter the number :"))
if num%3==0 and num%5==0:
    print("Divisible by both")
elif num%5==0:
    print("Divisible by 5")
elif num%3==0:
    print("Divisible by 3")
