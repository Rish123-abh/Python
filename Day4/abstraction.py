from abc import ABC ,abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self,side):
        pass
    @abstractmethod
    def area(self,side):
        pass


class Square(abstract):
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        print(f"Permeter of Square is {4*self.side}")
    def area(self):
        print(f"Area of square is {self.side*self.side}")
        
class Circle(abstract):
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        print(f"Permeter of circle is {2*3.14*self.radius}")
    def area(self):
        print(f"Area of circle is {3.14*self.radius*self.radius}")
obj=Circle(7)
obj.perimeter()
obj.area()

obj1=Square(4)
obj1.perimeter()
obj1.area()