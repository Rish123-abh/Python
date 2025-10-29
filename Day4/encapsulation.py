# Encapsulation means binding of methods and attributes in a single class
#  For this purpose specifier is used but protected is of no use in python deonted by _variablName
# eg _age

# Main use of private denoted by __variableName


class Factory:
    # Private Variable
    __city='Pune'

    def show(self):
        print(f"City name is {self.__city}")

obj=Factory()

# so in below we cant access the private attribute directly 
# print(obj.__city)
# Private member can be accessed within a class 
obj.show()