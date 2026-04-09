# 31
num=894
highest=0
while num>0:
    digit=num%10
    if digit>highest:
        highest=digit
    num=num//10
print(f'Highest digit is:{highest}')

# 32
num=894
lowest=9
while num>0:
    digit=num%10
    if digit<lowest:
        lowest=digit
    num=num//10
print(f'Lowest digit is:{lowest}')

# 33
num=1345
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
if sum%2==0:
    print(f'{sum} is even number')
else:
    print(f'{sum} is odd number')

