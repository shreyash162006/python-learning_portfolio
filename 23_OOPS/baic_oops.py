# object = a bundle of related attributes (varibales) and methods (functions)
#         Ex. phone , book , cup
#         we need a class to create an object

#class = (blueprint) used  to design the structure oand layout of an object

class car:
    def __init__(self , model , year , color , for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        #methods in a class
    def drive(self):
        print(f"You drive a {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.model} {self.color} ")

car1 = car( "BMW" , 2025 , "Black" , True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
car1.describe()