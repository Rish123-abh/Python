#strings 
a="A"
#ord is used to find a ascii code 
print(ord(a))
b="z"
print(ord(b))
c=65
# chr is used for converting code  to char  
print(chr(c))


# String Slicing 
demo="Hello"

#Positive Indexing -> 0,1,2,3,4 
#Negative Indexing -> -5,-4,-3,-2,-1
print(demo[3],demo[-1])

demoString="Hello World"
# startpoint:endpoint+1:steps
print(demoString[0:5:2])
print(demoString[-10:])
print(demoString[6:])