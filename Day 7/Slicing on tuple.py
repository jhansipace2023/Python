#Positive slicing

t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[0:5:1])
print(t1[1:7:1])
print(t1[2:8:2])
print(t1[0:9:3])
print(t1[3:9:2])
print(t1[4:9:1])
print(t1[1:9:2])
print(t1[0:8:4])
print(t1[2:9:3])
print(t1[5:9:1])

#Negative slicing
t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[-9:-1:1])
print(t1[-8:-2:1])
print(t1[-7:-1:3])
print(t1[-6:-2:1])
print(t1[-5:-1:2])
print(t1[-9:-3:2])
print(t1[-8:-1:1])
print(t1[-7:-3:2])
print(t1[-6:-1:2])
print(t1[-4:-1:1])

#Reversing
t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[::-1])
print(t1[2::-2])
print(t1[-2::-2])