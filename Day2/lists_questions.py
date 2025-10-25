# Questions on List 

# Print +ve and -ve numbers
l=[12,-23,34,-2,-23,5]

print("Positive Elements are ")
for i in l:
    if(i>=0):
        print(i)
print("Negative  Elements are ")
for i in l:
    if(i<0):
        print(i)



# Mean of list 

l=[1,2,3,4,5]
sum=0
for i in l :
    sum+=i
print(sum/len(l))    


# Find the greatest Element and its index


l=[12,3,4,234,2]
maxValue=float('-inf')
for i in l:
    if i>maxValue:
        maxValue=i
print(maxValue)
print(l.index(maxValue))

# Find second Largest Element 

l=[12,3,4,23,2,34,34]
largest=l[0]
second_largest=float('-inf')
for i in l: 
    if(i>largest):
        second_largest=largest
        largest=i
    elif i>second_largest and i<largest :
        second_largest=i    
print(largest)
print(second_largest)

# Check if List is sorted or not 
def checkSorted(list):
    for i in range(len(list)-1):
        if(list[i+1]<list[i]):
            return False
    return True
l=[1,2,3,4,6,2]

if(checkSorted(l)):
    print("Sorted List ")
else:
    print("Not Sorted List ")