class Factory: #Parentclass
    a="This is base class"
    def hello(self):
        print("Hello function in base class ")

#  Syntax for inheritance

class Factory2(Factory): #Child class
    def hello2(self):
        print("Hello function in derived class ")

obj = Factory2()

obj.hello()
obj.hello2()

# constructor of base class will  also can be used by child class
#  child class do not need to  define its constructor

class Animal():
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your name is {self.name}")    

# class Human(Animal):
#     pass

# obj = Human('Rishabh')
# obj.show()

# Now if need to add some more functionality to child class constructor then we can use super() function and will create 
# constructor in child class also
class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(f"Your Name is {self.name} and age is {self.age}")    

obj1=Animal('Jatin')
obj = Human('Rishabh',23)
obj.show()
obj1.show()



#Multiple Inheritance 
#Constructor will be in order in which it is inherited like if C(A,B)-> A constructor will be used  
#for C(B,A)-> B constructor will be called 

class A:
    def __init__(self,name):
        self.name=name
    name1='Rishabh'

class B:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    name2='Jatin'

class C(A,B):
    name3='Random'

obj=C('Random Guy')
print(obj.name)
print(obj.name3)
print(obj.name2)
print(obj.name1)



# Multilevel Inheritance

class A:
    name1='First base class '
class B(A):
    name2='First inherited class '
class C(B):
    name3='Last Inherited class '

obj=C()
print(obj.name1)
print(obj.name2)
print(obj.name3)



