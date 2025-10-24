# Function without parameter 
# def greet():
#     return "Hello, World!"

# print(greet())

# Function with parameter
# def greet(name):
#     print(f"Hi {name}")

# name=input("Enter name")
# greet(name)

def sum(a,b):
    print(f"Sum of a and b is {a+b}")

# Positional Arguments 
sum(2,3)


# Keywords Arguments 
def greet(name,age):
    print(f"Name is {name} and age is {age}")

greet(age=22,name="Sweety")


# Default Arguments 
def greet(name,age=24):
    print(f"Name is {name} and age is {age}")

greet(name="Sweety")
