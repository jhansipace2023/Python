# 44
num=6
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')

# 45
num=1124
sum=0
prod=1
temp=num
while num>0:
    digit=num%10
    sum=sum+digit
    prod=prod*digit
    num=num//10
if sum==prod:
    print(f'{temp} is a spy number')
else:
    print(f'{temp} is not a spy number')

# 46
string='smith'
i=0
while i<len(string):
    print(string[i],ord(string[i]))
    i=i+1

# 47
s='python'
i=0
result=' '
while i<len(s):
    if s[i]>='a' and s[i]<='z':
        result=result+chr(ord(s[i])-32)
    else:
        result=result+s[i]
    i=i+1
print(result)

# 48
s='PYTHON'
i=0
result=' '
while i<len(s):
    if s[i]>='A' and s[i]<='Z':
        result=result+chr(ord(s[i])+32)
    else:
        result=result+s[i]
    i=i+1
print(result)

# 49
s='python'
count=0
i=0
while i<len(s):
    count=count+1
    i=i+1
print(count)

# 50
s='pyspider'
ch='s'
i=0
count=0
while i<len(s):
    if s[i]==ch:
        count=count+1
    i=i+1
print(count)

# 51
s='education'
i=0
count=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        count=count+1
    i=i+1
print(count)

# 52
s='education'
i=0
vowels=0
consonant=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        vowels=vowels+1
    else:
        consonant=consonant+1
    i=i+1
print(f'count of vowels is:{vowels}')
print(f'count of consonants is:{consonant}')

# 53
s='pyTHon'
i=0
result=' '
while i<len(s):
    ch=s[i]
    if ch>='A' and ch<='Z':
        result=result+chr(ord(ch)+32)
    elif ch>='a' and ch<='z':
        result=result+chr(ord(ch)-32)
    else:
        result=result+ch
    i=i+1
print(result)

# 54
pin='1234'
balance=1000.00
attempts=0
while attempts<3:
    entered=input('enter the pin:')
    if entered==pin:
        break
    else:
        print('Wrong PIN')
else:
    print("Account locked")
    exit()
while True:
    print("\n1.Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    choice=input("choose: ")
    if choice=='1':
        print(f'Balance:{balance}')
    elif choice=='2':
        amt=float(input("Deposit: "))
        balance+=amt
    elif choice=='3':
        amt=float(input("Withdraw: "))
        if amt<=balance:
            balance-=amt
        else:
            print("Insufficient Funds")
    elif choice=='4':
        print('Goodbye!')
        break
    else:
        print("Invalid option")