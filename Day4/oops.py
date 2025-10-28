#  class name start with capital letter Factory good practice

class Factory:
    a=12 #attribute-> class attribute 
    # Constructor initialised 
    # this __init__ is a type of dunder method  means double underscore method
    def __init__(self,material,zip,pocket):
        self.material=material #instance attribute
        self.zip=zip
        self.pocket=pocket
        

# when obj calls hello function then python passes object as a parameter to hello function and self take this object as a prameter so
#  if self is not present in hello function then will throw error
# basicaly when obj calls class then obj is passed by default as a self in function and self takes object as a  paramerter 
    def show(self): #method-> instance method 
        print(f" Your details {self.material} ,{self.pocket} and {self.zip} ")

    # class method 
    #  @->decorator
    @classmethod
    def hello(cls):
        print(f"This is class method {cls.a}")
        # below line will not work since it cannot access the instance variables 
        # print(f"This is class method {cls.material}")

    #static method 
    @staticmethod
    def static():
        print("This is a static method")
    print("This is first factory class initialised ")    

reebok=Factory("Leather",2,4)
campus=Factory("Plastic",3,5)

# print(obj.a)
# obj.hello()

reebok.hello()
reebok.show()
reebok.static()
