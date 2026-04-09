# 19
nums=[10,20,45,98,35]
highest=nums[0]
for i in nums:
    if i>highest:
        highest=i
print(highest)

# 20
nums=[10,20,45,98,35]
lowest=nums[0]
for i in nums:
    if i<lowest:
        lowest=i
print(lowest)

# 21
nums=[10,20,45,98,35]
second_highest=highest=float('-inf')
for i in nums:
    if i>highest:
        second_highest=highest
        highest=i
    elif i>second_highest and i!=highest:
        second_highest=i
print(second_highest)

# 22
text='eye'
rev=''
for ch in text:
    rev=ch+rev
if rev==text:
    print(f'{text} is a palindrome')
else:
    print(f'{text} is not a palindrome')

# 23
s1='education'
result=''
for ch in s1:
    result=result+ch
print(result)

# 24
input_str='education123python'
result=''
for ch in input_str:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        result=result+ch
print(result)

# 25
input_str='education123python'
alphabet='' 
digit=''
for ch in input_str:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        alphabet=alphabet+ch
    elif '0'<=ch<='9':
        digit=digit+ch
print(alphabet)
print(digit)

# 26
input_str='PyThoN'
result=''
for ch in input_str:
    if 'A'<=ch<='Z':
        lowest=chr(ord(ch)+32)
        result=result+lowest
    else:
        result=result+ch
print(result)

# 27
input_str='PyThoN'
result=''
for ch in input_str:
    if 'A'<=ch<='Z':
        lowest=chr(ord(ch)+32)
        result=result+lowest
    elif 'a'<=ch<='z':
        upper=chr(ord(ch)-32)
        result=result+upper
print(result)

# 28
input_str='EDUCATION'
result=''
for ch in input_str:
    if ch in 'AEIOU':
        lowercase_char=chr(ord(ch)+32)
        result+=lowercase_char
    else:
        result+=ch
print("Result:",result)

# 29
input_str="Welcome To Python"
uppercase_chars=''
for ch in input_str:
    if 'A'<=ch<='Z':
        uppercase_chars=uppercase_chars+ch
print("Uppercase characters:",uppercase_chars)

# 30
input_str='Welcome To Python'
lowercase_chars='' 
for ch in input_str:
    if 'a'<=ch<='z':
        lowercase_chars=lowercase_chars+ch
print("Lowercase characters:",lowercase_chars)

# 31
input_str="User123"
digits=''
for ch in input_str:
    if '0'<=ch<='9':
        digits+=ch
print("Digits in the string:",digits)

# 32
input_str="Hello @ python"
special_chars=''
for ch in input_str:
    if not(('A'<=ch<='Z')or('a'<=ch<='z')or('0'<=ch<='9')):
        if ch!=' ':
            special_chars+=ch
print("Special Characters:",special_chars)

# 33
s="Hello 123 python"
result=''
for ch in s:
    if ch in 'AEIOUaeiou' or ch==' ':
        result+=ch
print(result)

# 34
s="Hello 123 python"
vow=''
con=''
digit=''
for ch in s:
    if ch in 'AEIOUaeiou':
        vow=vow+ch
    elif ch not in 'AEIOUaeiou' and not ch.isdigit():
        con=con+ch
    elif '0'<=ch<='9':
        digit=digit+ch
print("Vowels:",vow)
print("Consonants:",con)
print("digits:",digit)

# 35
input_str='Python'
lowercase_chars=''
for ch in input_str:
    if 'a'<=ch<='z':
        lowercase_chars+=ch
print("Lowercase characters:",lowercase_chars)

# or Using method
string='PYspiders'
s1=''
for char in string:
    if char.islower():
        s1+=char
print(s1)

# 36
string='python123jspiders'
s1=''
for char in string:
    if char.isdigit():
        s1=s1+char
print(s1)

# 37
string="hello good evening"
out=''
for i in string:
    if i==' ':
        out=out+'_'
    else:
        out=out+i
print(out)

# or Using issapace method

string="hello good evening"
out=''
for i in string:
    if i.isspace():
        out=out+'_'
    else:
        out=out+i
print(out)

# 38
string='python'
s1=''
for char in string:
    if char not in 'aeiou':
        s1=s1+char
print(s1)

# 39
num=145
total=0
for i in str(num):
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    total=total+fact
if total==num:
    print(f'{num} is strong number')
else:
    print(f'{num} is not strong number')

# 40
num=6
sum=0
temp=num
for i in range(1,num):
    if num%i==0:
        sum+=i
if temp==sum:
    print(f'{temp} is a perfect number')
else:
    print(f'{temp} is not a perfect number')

# 41
num=1124
sum=0
prod=1
for digit in str(num):
    sum=sum+int(digit)
    prod=prod*int(digit)
if sum==prod:
    print(f'{num} is a spy number')
else:
    print(f'{num} is not a spy number')

# 42
num=10
a=0
b=1
for i in range(10):
    print(a,end=' ')
    a,b=b,a+b

# 43
a=9
n=a*a
sum=0
for digit in str(n):
    sum=sum+int(digit)
if sum==a:
    print(a,"is a Neon number")
else:
    print(a,"is nota Neon number")