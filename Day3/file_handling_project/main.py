# File Handling Project 


# This is a way to import something which is different from js  
from pathlib import Path
import os
global_script_path=Path(__file__).parent
print(global_script_path)


def readfileandfolder():
    # This will take the path automatically for  directory in which file exist  
    script_path=Path(__file__)
    path = script_path.parent

    # This below will take  current working directory 
    # path=Path('')
    # path=Path('Day3/file_handling_projects')
    items=list(path.rglob('*')) 
    for i,items in enumerate(items):
        print(f"{i+1}: {items.name}") 

def createfile():
    try:
        readfileandfolder()
        filename=input("Enter the file name you want to create ")
        script_path=global_script_path/filename
        path = script_path
        if not path.exists():
            # here with keyword automatically handles the case to close the file automatically we dont need to do this manually 
            with open(path,'w') as fs:
                data= input("What you want to write ")
                fs.write(data)
            print("File created successfully")
        else:
            print("File already Exists")    
    except Exception as err:
        print(f"Error occurred as {err}")

def readfile():
    try:
        readfileandfolder()
        filename=input(print("Write a file name you want to read "))
        path= global_script_path/filename
        if  path.exists() and path.is_file():
            with open(path) as fs:
                print(fs.read())
                print('file read successfully!!')
        else:
            print("File do not exist")        
    except Exception as err:
        print(f"Exception occurs due to {err}")

def updatefile():
    try:
        readfileandfolder()
        filename=input("Enter the file name you want to update ")
        path=global_script_path/filename
        if path.exists() and path.is_file():
            print("Press 1 for updating file name ")
            print("Press 2 for overwriting  file content ")
            print("Press 3 for appending  file content ")
            choices=int(input("Select your choice "))

            if  choices==1:
                newname=input("Enter the new file name ")
                newpath=global_script_path/newname
                path.rename(newpath)
                print("File name updated successfully")   
            elif  choices==2:
                with open(path,'w') as f:
                    data=input("Enter the data you want to overwrite ")
                    f.write(data)
                    print("Data updated Succesfully")
            else:
                with open(path,'a') as fs:
                    data=input('Enter the data you want to append ')
                    fs.write(data)
                    print("Data appended  Succesfully")
        else:
            print("File do not exist")
    except Exception as err:
        print(f"Error Occured due to {err}")        

def deletefile():
    try:
        readfileandfolder()
        filename=input("Enter the file name you want to delete")
        path=global_script_path/filename
        if path.exists() and path.is_file() :
            os.remove(path)
            print('File removed succesfully')
        else:
            print("File does not exist")
    except Exception as err:
        print(f"Error occured due to {err}")


print("Press 1 for creating a file")
print("Press 2 for Reading a file")
print("Press 3 for updating a file")
print("Press 4 for Deleting a file")


userinput=int(input("Enter the number for the Operation you want!"))

if userinput==1:
    createfile()
if userinput==2:
    readfile()
if userinput==3:
    updatefile()
if userinput==4:
    deletefile()
