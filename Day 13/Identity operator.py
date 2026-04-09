a=98
b=98
print(id(a))
print(id(b))

a=98
b=98
print(a is b)
print(a is not b)

s1='python'
s2='java'
print(s1 is s2)
print(s1 is not s2)

s1='python'
s2='python'
print(s1 is s2)
print(s1 is not s2)

list1=[10,20,30]
list2=[10,20,30]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)