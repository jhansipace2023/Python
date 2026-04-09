# 1
n=int(input("Enter the number:"))
if n>5:
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    print(n)

# 2
ch=input()
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    if ch in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonent")
else:
    if '0'<=ch<='9':
        print("digit")
    else:
        print("not a digit")