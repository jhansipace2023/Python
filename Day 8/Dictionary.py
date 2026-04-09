d1 = {'a':10,'b':20,'c':30}
print(d1)
print(type(d1))

# Example 2
data = {'ename':'smith','salary':98000,'job':'analyst'}
print(type(data))

print(data.keys())
print(data.values())
print(data.items())


# Nested dictionary example

employees = {
    'emp1':{'ename':'smith','sal':98000},
    'emp2':{'ename':'martin','sal':95000},
    'emp3':{'ename':'scott','sal':45000},
    'emp4':{'ename':'allen','sal':38000},
    'emp5':{'ename':'jones','sal':785000}
}

# 1) WAP to print employee 3 information
print(employees['emp3'])

# 2) WAP to print name of 3rd employee
print(employees['emp3']['ename'])

# 3) WAP to print emp2 information
print(employees['emp2'])

# 4) WAP to print emp4 & emp5 information
print(employees['emp4'], employees['emp5'])

# 5) WAP to print name of 4th employee & salary of 5th employee
print(employees['emp4']['ename'], employees['emp5']['sal'])

# 6)
print(employees.keys())

print(employees['emp1'].keys())