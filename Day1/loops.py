# For Loop
# startpoint,endpoint+1,steps
for i in range(1,11,2):
    print(i)
    # Startpoint and step is set to default as 0 and 1 respectively
for i in range(11):
    print(i)
for i in range(-3,-16,-1):
    print(i)
for i in range(20,1,-1):
    print(i)

    # Table of 5 
    for i in range(1,11):
        print(5*i)  
a=[1,2,3,4,5]
for i in a:
    print(i)

a="Hello"
for i in range(len(a)):
    print(a[i])
for i in a:
    print(i)


# Break and continue 

for i in range(21):
    if i==15:
        break
    else:
        print(i)

for i in range(21):
    if i==3:
        continue
    print(i)

#Else-> This will run when break not executed otherwise it will skip 
# in below case else will executed 
for i in range(21):
    if i==146:
        print(i)
        print("Break Executed")
        break
else:
    print("Break Not Executed")

