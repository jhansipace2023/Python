# 28
num=1234
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

# 29
num=191
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print(f'{num} is an palindrome number')
else:
    print(f'{num} is not an palindrome number')


# 30
n=1
while n<=100:
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if n==rev:
        print(n)
    n=n+1





























