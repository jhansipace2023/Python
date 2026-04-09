# 17
n = 15

while n <= 21:
    print(n)
    n = n + 1

# 18
n = 1

while n <= 20:
    if n % 3 == 0:
        print(n, end=' ')
    n = n + 1

# 19
n = 1

while n <= 20:
    if n % 3 == 0 and n % 5 == 0:
        print(n, end=' ')
    n = n + 1


# 20
n1 = 25

while n1 <= 29:
    n2 = n1 % 10
    if n2 >= 6 and n2 <= 9:
        print(n1)
    n1 = n1 + 1

# 21
n = 348756

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit, end=' ')
    n = n // 10

# 22
n = 348756

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        print(digit, end=' ')
    n = n // 10

# 23
n = 348756

while n > 0:
    digit = n % 10
    if digit % 2 == 0 and digit > 4:
        print(digit, end=' ')
    n = n // 10

# 24
n = 5687
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print(total)

# 25
n = 5687
total = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total = total + digit
    n = n // 10

print(total)

# 26
n = 5872
pro = 1
sum = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum = sum + digit
    else:
        pro = pro * digit
    n = n // 10

print(sum)
print(pro)

#27
n = 5872
product = 1
sum = 0

while n > 0:
    digit = n % 10
    product = product * digit
    sum = sum + digit
    n = n // 10

print(f"product of digits : {product}")
print(f"sum of digits : {sum}")