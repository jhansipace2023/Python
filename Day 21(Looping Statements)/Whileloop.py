# 1
i=0
while i<=5:
    print(i)
    i=i+1

# 2
i=1
while i<=3:
    print("Hello Python")
    i=i+1

# 3
i=6
while i>=0:
    print(i,end=' ')
    i=i-1

# 4
i=1
while i<=10:
    if i%2==0:
        print(i,end=' ')
    i=i+1

# 5
i = 2
while i <= 10:
    print(i, end=' ')
    i = i + 2

# 6
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i, end=' ')
    i = i + 1

# 7
i = 1
while i <= 10:
    print(i)
    i = i + 2

# 8
num = 2
i = 1

while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i = i + 1

# 9
i = 1
total = 0

while i <= 5:
    total = total + i
    i = i + 1

print(total)

# 10
i = 1
total = 0

while i <= 10:
    if i % 2 == 0:
        total = total + i
    i = i + 1

print(total)

# 11
i = 1
total = 0

while i <= 10:
    if i % 2 != 0:
        total = total + i
    i = i + 1

print(total)

# 12
i = 1
even_total = 0
odd_total = 0

while i <= 10:
    if i % 2 == 0:
        even_total = even_total + i
    else:
        odd_total = odd_total + i
    i = i + 1

print(f"sum of even numbers is : {even_total}")
print(f"sum of odd numbers is : {odd_total}")

# 13
i = 1
prod = 1

while i <= 20:
    if i % 2 == 0:
        prod = prod * i
    i = i + 1

print(prod)

# 14
i = 1
prod = 1

while i <= 20:
    if i % 2 != 0:
        prod = prod * i
    i = i + 1

print(prod)

# 15
i = 1

even_sum = 0
odd_sum = 0
even_prod = 1
odd_prod = 1

while i <= 10:
    if i % 2 == 0:
        even_sum = even_sum + i
        even_prod = even_prod * i
    else:
        odd_sum = odd_sum + i
        odd_prod = odd_prod * i
    i = i + 1

print(f"sum of even numbers : {even_sum}")
print(f"sum of odd numbers : {odd_sum}")
print(f"product of even numbers : {even_prod}")
print(f"product of odd numbers : {odd_prod}")

# 16
i = 7956
count = 0

while i > 0:
    count = count + 1
    i = i // 10

print(count)