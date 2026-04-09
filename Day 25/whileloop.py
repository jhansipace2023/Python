# 34
num=5
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')

# 35
num=153
temp=num
sum_cubes=0
length=len(str(num))
while num>0:
    digit=num%10
    sum_cubes+=digit**length
    num=num//10
if temp==sum_cubes:
    print(f'{temp} is armstrong number')
else:
    print(f'{temp} is not armstrong number')
    

# 36
n=5
a,b=0,1
count=0
while count<n:
    print(a,end=' ')
    a,b=b,a+b
    count+=1


# 37
num=9
square=num*num
sum_digit=0
temp=square
while temp>0:
    digit=temp%10
    sum_digit+=digit
    temp=temp//10
if sum_digit==num:
    print(num,"is a neon number")
else:
    print(num,"is not a neon number")