# if else and if else if 

a=int(input("Enter the number "))
# str and int can be compared so firstly convert string input to int 
if(a>10):
    print("A is greater than 10")
    if a<20:
        print("A greater than 10 and less than 20")
    elif a>20 and a<25:
        print("A greater than 20 and less than 25")    
    else:
        print("A greater than 25")    

else:
    print("A is smaller than 10")
