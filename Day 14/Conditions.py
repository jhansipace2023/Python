#write a condition to check the given number is greater than 5
num = int(input("enter a number: "))
res = num>5
print(res)

#write a condition to check whether the given number is greater than 10 and less than 20
num = int(input("enter a number: "))
res = num>10 and num<20
print(res) 

#write a condition to check the given is divisible by 3
num = int(input("enter a number: "))
res = num%3 == 0
print(res)

#write a condition to check the given is divisible by both 3 & 5
num = int(input("enter a number: "))
res = num%3==0 and num%5==0
print(res)

#write a condition to check the given charactyer is uppercase
ch = input("enter a character: ")
res = ch>="A" and ch<="Z"
print(res)

#write a condition to check last digit of a given character is divisible by 3 or not
ch=input("enter a character: ")
ascii=ord(ch)
ls=ascii%10
res=ls%3==0
print(res)