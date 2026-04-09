#Positive slicing
r1=range(10,101,10)
updated=list(r1)
print(updated)       #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(updated[0:5])
print(updated[2:7])
print(updated[1:9:2])
print(updated[:5])
print(updated[5:])
print(updated[0:10:3])
print(updated[3:8])
print(updated[4:9:2])
print(updated[6:10])
print(updated[2:5])

#Negative Slicing
r1=range(10,101,10)
updated=list(r1)
print(updated) 

print(updated[-1])
print(updated[-3])
print(updated[-5:-1])
print(updated[-7:-2])
print(updated[-10:-5])
print(updated[-8:])
print(updated[:-3])
print(updated[-9:-4])
print(updated[-6:-3])
print(updated[-4:-1])

#Reversing
r1=range(10,101,10)
updated=list(r1)
print(updated) 

print(updated[::-1])
print(updated[6:2:-1])
print(updated[7::-1])
print(updated[3:-10:-1])
print(updated[5::-2])
print(updated[7:1:-3])
print(updated[9:-6:-1])
print(updated[-2:-9:-2])
print(updated[6:1:-1])
print(updated[-4::-3])