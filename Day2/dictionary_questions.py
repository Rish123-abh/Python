# Merge two lists 

l1={1:"Auto",2:"Car"}
l2={3:"Bus",4:"Rickshaw"}

l1.update(l2)
print(l1)

for i in l2:
    l1.update({i:l2[i]})
print(l1)    

for i in l2:
    l1[i]=l2[i]
print(l1)


# Count frequency of elements in list 

list=[1,2,3,4,2,4,3,2,1,4,5,2,3]
dict={}
for i in list:
    if(not dict.get(i)):
        dict[i]=1
    else:
        dict[i]+=1    
print(dict)    