
#  Exception Handling is used to tackle the errors
#  or exceptions gracefully without breaking the flow of code 


# else is simlar to what it is in for loop
# if exception occurs then else will not execute otherwise else will execute 
a=int(input("Enter the Number "))
try:
    print(f"{10/a} divison is done ")
except Exception as err:
    print(f"Error is occured due to {err}")    
else:
    print("Divison is done ")


# finally -> This will run no matter exception occurs or not 
a=int(input("Enter the Number "))
try:
    print(f"{10/a} divison is done ")
except Exception as err:
    print(f"Error is occured due to {err}")    
finally:
    print("Divison is done ")

# raise-> This allow us to throw error manually with our own customMessage

a=int(input("Enter the Number "))
try:
    if(a==0):
        raise ValueError("Denominator cannot be zero")
except Exception as err:
    print(f"Error is occured due to {err}")    
finally:
    print("Divison is done ")