# Accept two numbers and print greater 

a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))

if a>b:
    print(f"A is greater {a}")
else:
    print(f"B is greater {b}")

# Accept Gender and print message 
gender=input("Choose Your gender M or F")

if(gender=="M"):
    print("Good Evening Sir")
else:
    print("Good Evening Madam")

# Accept a number and check whether even or odd 

x=int(input("Enter the number"))
if x%2==0:
    print("Even Number")
else:
    print("Odd Number")

# Accept Name and age display valid voter or not

name=input("Enter Your name") 
age=int(input("Enter Your age"))

if(age>=18):
    print(f"Hey {name} you are a valid voter")
else:    
    print(f"Hey {name} you are not a valid voter")