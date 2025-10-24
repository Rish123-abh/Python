# Print Reverse Number from n to 1
# a=int(input("Enter The Number "))
# for i in range(a,0,-1):
#     print(i)


# Print sum upto n terms 
# a=int(input("Enter The Number "))
# sum=0
# for i in range(1,a+1):
#     sum+=i
# print(sum)    


# Factorial of a nummber
# a=int(input("Enter the number "))
# ans=1
# for i in range(1,a+1):
#     ans*=i
# print(ans)


# Print the sum of all even and odd numbers in  a range  separately 

# a=int(input("Enter first number of range"))
# b=int(input("Enter second number of range"))
# even=0
# odd=0
# for i in range(a,b+1,1):
#     if(i%2==0):
#         even+=i
#     else:
#         odd+=i
# print(even)
# print(odd)


# Check String is Palindrome or not 

# str=input("Enter the string ")
# first=0
# last=len(str)
# while first<=last:
#     if(str[first]!=str[last-1]):
#         print(False)
#         break
#     first+=1
#     last-=1
# else:
#     print(True)

# Reverse string 
# str=input("Enter the string ")
# ans=""
# last=len(str)-1
# while(last>=0):
#     ans+=str[last]
#     last=last-1
# print(ans)


# Separate Digit from number 
# num=int(input("Enter the number "))

# while(num!=0):
#     print(num%10)
#     num//=10


# Reverse a number 
# num=int(input("Enter the number "))
# ans=0
# while(num!=0):
#     ans=ans*10+(num%10)
#     num//=10
# print(ans)

import random
# Guess a number game 

num = random.randint(1,10)
tries=0
while True:
    guess=int(input("Enter a number between 1 to 10"))
    if(num==guess):
        tries+=1
        print(f"You guessed corrctly in {tries} tries")
        break
    elif num<guess:
        tries+=1
        print("Go a Little Lower ")    
    elif num>guess:
        tries+=1
        print("Go a Little Higher ")
    else:
        tries+=1
        print("You guessed Wrongly")        