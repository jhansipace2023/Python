# 1
for i in range(1,6):
    print(i,end=' ')


# 2
for i in range(5,0,-1):
    print(i,end=' ')

# 3
names=['Smith','martin','scott']
for name in names:
    print(name)

# 4
subject='python'
for ch in subject:
    print(ch)
    
# 5
for i in range(10,51,10):
    print(i)

# 6
for i in range(1,11):
    if i%2==0:
        print(f'{i} is even number')
    else:
        print(f'{i} is odd number')

# 7
for i in range(1,21):
    if i%2==0:
        print(i)

# 8
total=0
for i in range(1,11):
    total+=i
print(f'Sum of numbers:{total}')

# 9
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

# 10
num=3
for i in range(1,11):
    print(f'{num}*{i}={num*i}')

# 11
num=7438
count=0
for i in str(num):
    count=count+1
print(count)

# 12
num=7438
sum=0
for i in str(num):
    sum=sum+int(i)
print(sum)

# 13
num=123
prod=1
for i in str(num):
    prod=prod*int(i)
print(prod)

# 14
num=123
rev=0
for i in str(num):
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

# 15
num=7
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')

# 16
str='python'
count=0
for ch in str:
    if ch in 'AEIUOaeiou':
        count=count+1
print(count)

# 17
num=121
temp=num
rev=0
for i in str(num):
    
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==num:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')

# 18
num=153
temp=num
length=len(str(num))
sum=0
for i in str(num):
    if temp>0:
        digit=temp%10
        sum=sum+digit**length
        temp=temp//10
if sum==num:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not armstrong number')