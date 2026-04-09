# Reverse of a number
def reverse_num(num):
    rev=0
    
    for i in str(num):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev
print(reverse_num(1234567))

# Sum of digits
def sum_digit(num):
    sum=0
    for i in str(num):
        sum+=int(i)
    return sum
print(sum_digit(123))

# Palindrome or not
def palindrome(num):
    rev=0
    temp=num
    for i in str(num):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if temp==rev:
        return f'{temp} is palindrome'
    else:
        return f'{temp} is not palindrome'
print(palindrome(121))

# largest of two number
def largest(num1,num2):
    if num1>num2:
        return f'{num1} is largest number'
    else:
        return f'{num2} is largest number'
print(largest(3,2))

# Armstrong number
def armstrong(num):
    length=len(str(num))
    sum_cubes=0
    for i in str(num):
        sum_cubes=sum_cubes+int(i)**length
    if sum_cubes==num:
        return f'{num} is armstrong number'
    else:
        return f'{num} is not armstrong number'
print(armstrong(153))

# Strong number or not
def strong(num):
    sum=0
    for i in str(num):
        fact=1
        for j in range(1,int(i)+1):
            fact=fact*j
        sum=sum+fact
    if sum==num:
        return f'{num} is strong number'
    else:
        return f'{num} is not strong number'
print(strong(145))

# Perfect number or not
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        return f'{num} is perfect number'
    else:
        return f'{num} is not a perfect number'
print(perfect(6))

#fibonacci of n term
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b=b,a+b
    return a
fib(6)
