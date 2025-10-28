#  Compile time polymorphism not present in python 
# Run time polymorphism 
class Animal():
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your name is {self.name}")    
class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(f"Your Name is {self.name} and age is {self.age}")    

obj1= Animal('Jatin')
obj = Human('Rishabh',23)
obj.show()
obj1.show()
