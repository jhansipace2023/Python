# 38
list=[10,45,68,95,40]
i=0
result=0
while i<len(list):
    result=result+list[i]
    i=i+1
print(f'Sum of all elements is:{result}')

# 39
list=[10,45,68,95,40]
i=0
result=0
while i<len(list):
    if list[i]%2==0:
        result=result+list[i]
    i=i+1
print(f'Sum of all even digit elements is:{result}')

# 40
num=6
i=1
while i<=num:
    if num%i==0:
        print(i,end=' ')
    i=i+1

# 41
num=6
i=1
sum=0
while i<=num:
    if num%i==0:
        sum=sum+i
    i=i+1
print(sum)

# 42
num=5
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)

# 43
num=145
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
    print("Strong Number")
else:
    print("Not a strong number")