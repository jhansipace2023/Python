name='smith'
print(name)

name_87435="king"
print(name_87435) 

age=26
print(age)

#Check identifier is valid

name='scott'
print(name.isidentifier())

age=22
print(age.isidentifier())

name_123='tiger'
print(name_123.isidentifier())





#String formatting

ename='smith'
print(f'Hello {ename}')

ename='king'
salary=5000
print(f'employee name is:{ename} and he is earning salary:{salary}')