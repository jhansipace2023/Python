#To check the given number is greater
a=98
b=48
if a>b:
    print(f'a:{a} is greater than b:{b}')

#To check the given number is positive
num=eval(input("enter a number :"))
if num>0:
    print(f'{num} is positive')

#Or
num=98
if num>0:
    print(f'{num} is positive')

#To check the given number is even
num=46
if num%2==0:
    print(f'{num} is even number')

#To check the given number is odd
num=77
if num%2!=0:
    print(f'{num} is odd number')

#To check the number is divisible by 3
num=15
if num%3==0:
    print(f'{num} is divisible by 3')

#To check the number is divisible by 5
num=25
if num%5==0:
    print(f'{num} is divisible by 5')

#To check the number is divisible by 3 & 5
num=15
if num%3==0 and num%5==0:
    print(f'{num} is divisible by 3 & 5')

#To check the given string starts with vowels
s1='apple'
if s1[0] in 'aeiouAEIOU':
    print(f'{s1} starts with vowels')

#To check the given string starts with consonants
s2='microsoft'
if s2[0] not in 'aeiouAEIOU':
    print(f'{s2} starts with consonants')

#To check the given string ends with vowels
s3='Hello'
if s3[-1] in 'aeiouAEIOU':
    print(f'{s3} ends with vowels')

#To check the given string ends with consonants
s4='education'
if s4[-1] not in 'aeiouAEIOU':
    print(f'{s4} ends with consonants')

#To check the given string starts with uppercase
s5='Apple'
if s5[0] >= 'A' and s5[0] <= 'Z':
    print(f'{s5} starts with uppercase')

#or
s5='Apple'
if 'A'<=s5[0]<='Z':
    print(f'{s5} starts with uppercase')

#To check the given character is lowercase
ch='e'
if 'a'<=ch<='z':
    print(f'{ch} is lowercase')

#To check given character is digit
char='9'
if '0'<=char<='9':
    print(f'{char} is digit')

#To check the given character is special symbol
char='$'
if not('A'<=char<='Z' or 'a'<=char<='z' or '1'<=char<='9'):
    print(f'{char} is special symbol')