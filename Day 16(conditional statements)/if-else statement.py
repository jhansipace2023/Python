# 1
num=int(input("enter the number :"))
if num>5:
    print(num**2)
else:
    print(num**3)
print("Program End")

# 2
num=int(input("enter the number :"))
if 3<= num <= 7:
    print(num,num,num,sep='\n')
else:
    res=num%10
    print(res)
print("Program End")

# 3
num=int(input("Enter the number :"))
if num%3==0 and num%5==0:
    print(num+1)
else:
    print(num//10)
print("Program end")

# 4
num=int(input("Enter the number :"))
if 12%num==0 and 16%num==0:
    print(12+16)
else:
    print(16-num)

# 5
ch=input("Enter the character :")
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    print(ord(ch))
else:
    print(ch)

# 6
ch=input("Enter the character :")
if (('A'<=ch<='Z' or 'a'<='z') and ch not in 'aeiouAEIOU'):
    print(ch)
else:
    ascii=ord(ch)
    ld=ascii%10
    print(ld)
