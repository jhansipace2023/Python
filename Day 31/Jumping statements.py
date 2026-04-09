# Break Statement
# 1
for i in range(1,21):
    if i==5:
        break
    print(i,end=' ')

# 2
for i in 'abcdefghijk':
    if i=='e':
        break
    print(i)

# 3
for num in range(1,21):
    if num%7==0:
        break
    print(num,end=' ')

# Continue statement
# 1
for num in range(1,6):
    if num==3:
        continue
    print(num,end=' ')

# 2
for num in range(1,11):
    if num%2==0:
        continue
    print(num,end=' ')

# 3
for num in range(1,11):
    if num%2!=0:
        continue
    print(num,end=' ')

# Pass statement
for num in range(6):
    pass
print('Done')