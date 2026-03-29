#super() = Function used in a child class to call methods from a parent class (superclass).
#          Allows u to extend the functionality of the inherited methods

class Shape:
    def __init__(self , color , is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
      def __init__(self , color , is_filled, radius): 
        super(). __init__(color , is_filled)
        self.radius = radius 

class Square(Shape):
    def __init__(self , color , is_filled , height , width ):
        super(). __init__(color , is_filled)
        self.height = height
        self.width = width

class Traingle(Shape):
    def __init__(self , color , is_filled , width , height):
        super(). __init__(color , is_filled)
        self.height = height
        self.width = width

circle = Circle(color = "red" , is_filled = True , radius = 5)
print(circle.radius)
print(circle.color)