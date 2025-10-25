# List is ordered mutated dupliates and heterogeneous
# List is similar to  array in js 
# list=[12,12,23,34,"Hello"]
list=[12,12,23,34]

print(list[len(list)-1])
print(list[1:4:])
print(list[-2])

# Traversing on List 
# Based on index 
for i in range(len(list)):
    print(f"Element at index {i} is {list[i]}")

# Directly Iterate on Element 

for i in list:
    print(i)


# Methods on List 

# Allows to add single element in end 
list.append(20)
print(list)
# insert allows to add element at specific position 
list.insert(1,2332)
print(list)
# Extend add multiple elements at end 
list.extend([20,25,30])
print(list)

# Removes first Occurence 
list.remove(12)
print(list)

# Removes and store the elemnet at given index 
popped_element=list.pop(0)
print(list)
print(popped_element)

print(list.index(20))
print(list.count(20))

list.sort()
print(list)
newList=list.copy()
print(f"New List {newList}")
list.reverse()
print(list)
list.clear()
print(list)

import copy

list1=[[1,2],3]
print(list1)
#  This is used for a shallow copy will not copy nested Objects 
list2=list1.copy()
print(list2)
#  This is used for a deep copy will not copy nested Objects 
list2=copy.deepcopy(list1)
list2[0].append(10)
print(list1)
print(list2)






