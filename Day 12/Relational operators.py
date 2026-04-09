a=98
b=98
print(a==b)

a=98
b=45
print(a==b)

s1='jspiders'
s2='Jspiders'
print(s1==s2)

list1=[10,20,30]
list2=[10,20,30]
print(list1==list2)

a=98
b=100
print(a!=b)

s1='python'
s2='java'
print(s1>s2)

print(ord('p'))
print(ord('j'))

s3='apple'
s4='microsoft'
print(s4>s3)

#To find the ascii value of alphabet A
char='A'
print(ord(char))

#To find the ascii value of alphabet a
char='a'
print(ord(char))

#To convert upper case into lower case
s1='A'
result=ord(s1)+32
print(chr(result))

#To convert lower case into upper case
s2='a'
result=ord(s2)-32
print(chr(result))

#To swap two numbers without using third variable
a=5
b=10
print(f'before swapping a={a} and b={b}')
a,b=b,a
print(f'after swapping a={a} and b={b}')

#To swap two numbers using third variable
a=5
b=10
print(f'before swapping a={a} and b={b}')
temp=a
a=b
b=temp
print(f'after swapping a={a} and b={b}')