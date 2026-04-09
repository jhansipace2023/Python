#Positive slicing
lst=[10,"python",3.14,True,[1,2],{"a":1},(5,6)]
print(lst[0:3:1])
print(lst[1:4:1])
print(lst[2:6:1])
print(lst[3:7:1])
print(lst[0:4:1])
print(lst[2:7:1])
print(lst[0:7:2])
print(lst[1:6:2])
print(lst[0:7:3])
print(lst[4:7:1])

#Negative Slicing
lst=[10,"python",3.14,True,[1,2],{"a":1},(5,6)]
print(lst[-7:-4:1])
print(lst[-6:-3:1])
print(lst[-5:-2:1])
print(lst[-4:-1:1])
print(lst[-3:7:1])
print(lst[-7:7:2])
print(lst[-5:6:1])
print(lst[-4:6:1])
print(lst[-7:-1:1])

#Reverse Slicing
lst=[10,"python",3.14,True,[1,2],{"a":1},(5,6)]
print(lst[6::-1])
print(lst[6:0:-1])
print(lst[5:1:-1])
print(lst[4::-1])
print(lst[6:2:-2])