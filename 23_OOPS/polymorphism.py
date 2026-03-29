# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritence = An object could be treated of the same type as a parent class
#               2. "Duck typing" = Object must have necessary attributes /methods

from abc import ABC , abstractmethod
class Shape :
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

class Square(Shape):
    def __init__(self , side):
        self.side = side
    def area(self):
        return self.side*self.side
class Traingle(Shape):
    def __init__(self , base , height ):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5*self.base*self.height
    
class Pizza(Circle):
    def __init__(self , topping , radius ):
        self.topping = topping
        super().__init__(radius)



shapes = [ Circle(5) , Traingle(4, 5) , Square(6)  , Pizza("pepperoni" , 15 )]


for shape in shapes:
    print(f"{shape.area()} cm2")



