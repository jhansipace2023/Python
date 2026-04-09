# General copy
# 1
list1=[10,20,30,40]
list2=list1
print(list1)
print()
print(list2)

# 2
list1=[10,20,30,40]
list2=list1
print(id(list1))
print()
print(id(list2))

# Modification of element in copied object
# 3
list1=[10,20,30,40]
list2=list1
list2[3]=98
print(list1)
print()
print(list2)

# Shallow Copy
import copy
original_list=[10,20,[1,2,3,4]]
shallow_copy_list=copy.copy(original_list)
shallow_copy_list[2][3]=98
print(original_list)
print()
print(shallow_copy_list)

# Deep Copy
import copy
original_list=[10,20,[1,2,3,4]]
deep_copy_list=copy.deepcopy(original_list)
deep_copy_list[2][3]=98
print(original_list)
print()
print(deep_copy_list)