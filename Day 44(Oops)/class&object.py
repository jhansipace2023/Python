# 1
# creating class
class employee:
    ename='smith'
    sal=98000
    job='analyst'
# creating object for class
e1=employee()
# accessing class variables using object
print(f'employee name : {e1.ename}')
print(f'employee salary : {e1.sal}')
print(f'designation : {e1.job}')

# 2
class employee:
    pass
e1=employee()
e1.ename='smith'
e1.sal=5000
e2=employee()
e2.ename='king'
e2.sal=9000
print(f'First employee name : {e1.ename} and salary : {e1.sal}')
print(f'Second employee name : {e2.ename} and salary : {e2.sal}')

# 3
class student:
    name='abc'
    phno=1234567890
    email='abc@gmail.com'
    sub1='SQL'
    sub2='Python'
    sub3='Web'
s1=student()
print(f'Student name : {s1.name}')
print(f'Student phno : {s1.phno}')
print(f'Student mailID : {s1.email}')
print(f'Subjects are : {s1.sub1},{s1.sub2},{s1.sub3}')

# 4
class cars:
    pass
c1=cars()
c1.name='BMW'
c1.color='Red'
c2=cars()
c2.name='tesla'
c2.color='Black'
c3=cars()
c3.name='Benz'
c3.color='White'
print(f'First Car name is : {c1.name} and color is : {c1.color}')
print(f'Second Car name is : {c2.name} and color is : {c2.color}')
print(f'Third Car name is : {c3.name} and color is : {c3.color}')