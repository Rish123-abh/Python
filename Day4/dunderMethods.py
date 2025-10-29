class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # dunder method will return things 
    def __str__(self):
        return f"String dunder method is called {self.name}"
    def __add__(self,other):
        # unpacking tuple 
        a,b=other
        return f"add  dunder method is called {self.age+a.age+b.age}"
        # return f"add  dunder method is called {self.age+other.age}"
    
obj1=Animal('lion',12)
obj2=Animal('Dolphin',14)
obj3=Animal('Whale',13)
print(obj1)
print(obj1+(obj2,obj3))