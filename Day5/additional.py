#  args kwargs 
# *args will return tuple  with this it will take multiple arguments we can pass any number of arguments inside function 
# **kwargs will return dictionary will take key words  -> will take any number of key value pairs 


def addition(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    return sum 



print(addition(1,2))
print(addition(1,2,3))
print(addition(1,2,3,4))



def information(**kwargs):
    print(kwargs)
    for i in kwargs:
        # end keyword  is used here to print all thing in same line 
        print(f"{i}:{kwargs[i]}",end=" ")


information(name="Rishabh",age=23,designation='Developer')



# Single line for ternary Operator thing 

a=13
print("even" if a%2==0 else "odd")


# list comprehension 

# Traditional Way 
# even=[]
# for i in range(31):
#     if i%2==0:
#         even.append(i)
# print(even)

# comprehensive way 

# what we need to add in list is passed at first place 
even=[i for i in range(31) if i%2==0]
print(even)


# dictionary comprehension 

l={i:i*i for i in range(21) if i%2==0}
print(l)


# this lambda function is mostly used in numpys and pandas 
# Lambda function -> this is used for creating inline function contains only single expression 

# normal function 
# def addition(a,b):
#     print(a+b)

# addition(1,2)


addition=lambda a,b:a+b

print(addition(2,4))
# Lambda function can take multiple arguments as well here sum is inbuilt function 
addition=lambda *args:sum(args)

print(addition(2,4,3,4))

# we can also use if else 

even_or_odd=lambda a:"even" if a%2==0 else "odd"

print(even_or_odd(15))


#  using map 
# func  is function of doing trnasformation and list is used as a parameter for that function 
# map(func,list)

numbers=[1,2,3,4,5]
result=list(map(lambda x:x*2,numbers))
print(result)

#  we can do with simple function also 
def doubled(num):
    return num*2
numbers=[1,2,3,4,5]
result=map(doubled,numbers)
print(list(result))



# filter 

result=filter(lambda x:x%2==0,numbers)
print(list(result))



# modules and packages 

# modules  is like a file which contains python code and we can use that code in other files by importing that module
# package is a collection of modules (diff files)

# importing module Math which is file containing functions
# import Math -> for single module file 
from packages import Math,hello # to use different module from a package 
print(Math.additon(2,3))
print(Math.subtraction(2,3))

hello.hello()
