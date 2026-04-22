# 1 WAP to print sequence of numbers from 1 to 5
num=[a for a in range(1,6)]
print(num)

# 2
num=[a*a for a in range(1,6)]
print(num)

# 3
num=[num for num in range(1,11) if num%2==0]
print(num)

# 4
li=[10,35,40,65,20,30,45]
even_num=[num for num in li if num%2==0]
print(even_num)

# 5
num=[num for num in range(1,11) if num%2!=0]
print(num)

# 6
li=[10,35,40,65,20,30,45]
odd_num=[num for num in li if num%2==0]
print(odd_num)

# 7
words=['python','java','sql']
result=[w.upper() for w in words]
print(result)

# 8
words=['python','java','sql']
result=[f'{w}:{len(w)}' for w in words]
print(result)

# 9
nums=[a*a for a in range(1,11) if a%2==0]
print(nums)

# 10
nums=[0 if num%2==0 else num for num in range(1,11)]
print(nums)

# 11
string='python'
chars=[ch for ch in string]
print(chars)

# 12
nums={a:a*a for a in range(1,6)}
print(nums)

# 13
nums={a:a*a for a in range(1,11) if a%2==0}
print(nums)

# 14
data={'a':1,'b':2,'c':3}
result={v:k for k,v in data.items()}
print(result)

# 15
words=['python','java','sql']
result=[w[::-1] for w in words]
print(result)

# 16 Student marks analyzer using comprehension
students={
    'smith':82,
    'scott':67,
    'martin':39,
    'allen':91,
    'ford':45,
    'miller':28,
    'virat':76
}
# Dictionary comprehension for result(pass/fail)
result={name:("Pass" if marks>=40 else "Fail") for name,marks in students.items()}
# Dictionary comprehension for grades
grades={
    name:(
        "A" if marks >= 75 else
        "B" if marks >= 60 else
        "C" if marks >= 40 else
        "F"
    )
    for name,marks in students.items()
}
# List of passed students
passed_students=[name for name,status in result.items() if status=="Pass"]
# List of failed students
failed_students=[name for name,status in result.items() if status=="Fail"]
# Bonus list for toppers
toppers=[name for name,marks in students.items() if marks>=75]
print(f'Result:{result}')
print(f'Grades:{grades}')
print(f'Passed students : {passed_students}')
print(f'Failed students : {failed_students}')
print(f'Toppers(Bonus List):{toppers}')