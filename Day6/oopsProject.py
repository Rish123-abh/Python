
#  Creating  oop project for banking system 
import random 
import json
import string 
from pathlib import Path
class Bank:
    database='Day6/data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print('No Such file exists')
    except Exception as err:
            print(f"Error Occured du eto {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices('!@#$%^&*',k=1)
        id= alpha+num+spchar
        # This shuffle returns list 
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):    
        info = {
            "name": input("Tell your name :- "),
            #  if in below we try to give something string then it will give error 
            "age" : int(input("tell your age :- ")),
            "email": input("tell your email :- "),
            "pin": int(input("tell your 4 number pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            # "accountNo." : 1234,
            "balance" : 0
        }
        
        if(info['age']<18 or len(str(info['pin']))!=4):
            print("Cannot create an account ")
        else:
            print(" Account created successfully ")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Note your account Number ") 

            # need to update data 
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber=input("Tell your account number ")
        pin=int(input("Tell your pin "))
        userdata=[i for i in Bank.data if i["accountNo."]==accnumber and i["pin"]==pin]
        if not userdata:
            print("No details found ")
        else:
            try:    
                deposit=int(input("Enter the money you want to deposit "))
                if deposit>10000 or deposit<0:
                    print('Sorry cant deposit money it is not between 0 and 10000')
                else:
                    userdata[0]["balance"]+=deposit
                    Bank.__update()
                    print("Money deposited successfully")
                    print(f"Updated Balance is {userdata[0]["balance"]}") 
            except Exception as err:
                print(f"Money must be in number")
    def withdrawmoney(self):
        accnumber=input("Tell your account number ")
        pin=int(input("Tell your pin "))
        userdata=[i for i in Bank.data if i["accountNo."]==accnumber and i["pin"]==pin]
        if not userdata:
            print("No details found ")
        else:
            withdraw=int(input("Enter the money you want to withdraw "))
            if withdraw>userdata[0]['balance'] or withdraw<0:
                print(f"Sorry cant withdraw money it is not between 1 and {userdata[0]['balance']} ")
            else:
                userdata[0]["balance"]-=withdraw
                Bank.__update()
                print("Money Withdrawn successfully")
                print(f"Updated Balance is {userdata[0]["balance"]}") 

    def showdetails(self):
        accnumber=input("Tell your account number ")
        pin=int(input("Tell your pin "))
        userdata=[i for i in Bank.data if i["accountNo."]==accnumber and i["pin"]==pin]
        if not userdata:
            print("No details found \n")
        else:
            print(f"Your details are")
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")


    def updatedetails(self):
        accnumber=input("Tell your account number ")
        pin=int(input("Tell your pin "))
        userdata=[i for i in Bank.data if i["accountNo."]==accnumber and i["pin"]==pin]
        if not userdata:
            print("No details found \n")
        else:
            try:
                print("you cannot change the age, account number, balance")
                print("Fill the details for change or leave it empty if no change")
                new_name=input("Enter new name or press enter ")
                new_email=input("Enter new email or press enter ")
                new_pin=int(input("Enter new pin or press enter "))
                if new_name!="":
                    userdata[0]['name']=new_name
                if new_email!="":
                    userdata[0]['email']=new_email
                if new_pin!="":
                    if(len(str(new_pin))!=4):
                        print("Enter pin of length 4 ")
                    else:
                        userdata[0]['pin']=new_pin

                Bank.__update()
                print("Details updated successfully")
            except Exception as err:
                print("Enter the numerical pin !!!")
    def deleteaccount(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata :
            print("sorry no such data exist ")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()


user=Bank()

print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.createaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.deleteaccount()