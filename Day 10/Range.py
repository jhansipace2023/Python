r1=range(11)
print(r1)

r2=range(11)
print(list(r2))

r3=range(6)
print(tuple(r3))

#Example for start & stop
r4=range(1,7)
updated=list(r4)
print(updated)

r5=range(10,17)
print(tuple(r5))

#Example for start,stop & step
r6=range(1,7,1)
print(list(r6))

r7=range(1,11,2)
print(list(r7))

r8=range(2,11,2)
print(list(r8))

r9=range(10,101,10)
print(list(r9))

#Example to generate sequence of numbers in descending order
r1=range(10,0,-1)
print(list(r1))

r2=range(10,0,-2)
print(list(r2))

r3=range(10,0,-3)
print(list(r3))