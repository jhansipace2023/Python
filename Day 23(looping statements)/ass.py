#write a program to check given number is palindrome

num=191
rev=0
temp=num
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')



