# Tuples -> Immutable ,duplicates , ordered ,heterogenous
# This does not have much Use case 
a=(1,2,3,4,4)
print(type(a))
# value change not allowed immutable 
# a[0]=3
# print(a[0])

#  Traversing in same way as list 

for  i  in a:
    print(i)

for i in range(len(a)):
    print(a[i])


# There are two methods only 

print(a.index(4))
print(a.count(4))

# Tuple Unpacking 

a,b,c,d=(1,2,3,4)
print(a,b,c,d)
# a=(1) this will give int as a type
# a=(1,) this will give as a tuple type 
print(type(a))  
