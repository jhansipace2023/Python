a=98
b=10
print(a>b and b<a)

a=97
b=11
print(a>b or b>a)

a=11
b=95
print(a>b or a==b)

a=98
b=10
print(not(a>b))

a=100
b=100
print(not(a!=b))

a=100
b=90
c=60
print(a>b and b>c and c<a)

a=100
b=50
c=30
print(a>b or b<c or c>a)

a=80
b=60
c=10
print(not(a>b)and(b>c))