# Dictionary -> Mutable ,Heterogenous -> key value pair -> key should be unique and immutable -> only string, number and tuples are allowed as key  Order->Dictionary follows insertion order

# Dictionary is similar to map in js 

# Keys cannot  be changed CRUD operations can be performed  on value only 
# Empty dictionary
# d={}
# print(type(d))

d={1:"Rishabh",2:"Jatin"}
print(type(d))
print(d)
print(d[1])


d[1]="Rishabh Agrawal"
print(d)

# Updation and creation 
# d[3]="Lalit Agrawal"
d.update({3:"Lalit Agrawal"})
print(d)

# Deletion 
del d[3]
print(d)

# Iteration on Dictionary

# for i in d:
#     print(f"{i}:{d[i]}")

for i in d.values():
    print(i)

import copy 
# Methods in Dictionary 
a={1:"Car",2:"Bike",3:"Auto",4:{1:"Truck"}}
print(a)
print(a.get(1))

# a.clear()
# print(a)

# Shallow Copy 
b=a.copy()



# Deepcopy 
b=copy.deepcopy(a)
b[4][1]="AutoCar"
print(b)
print(a)

# Give all items 
print(a.items())

# It returns the value and remove key value pair
print(a.pop(1))
print(a)

# It returns key value pairs in LIFO order and remove it from list 
print(a.popitem())
print(a)


