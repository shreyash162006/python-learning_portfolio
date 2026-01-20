# using the module created by me 

import mymodule as m

pie = m.pi
print(pie)
num = int(input("Enter any number : "))
square = m.square(num)
print(f"The square of the {num} is : {square}")

cube = m.cube(num)
print(f"The cube of the {num} is : {cube}")

sqrt = m.square_root(num)
print(f"The square root of {num} is : {sqrt}")
# circle functions 
radius = float(input("Enter the radius of the circle : "))

circumference = m.circumference(num)
print(f"The circumference of the circle having radius {radius} is : {circumference}")

area = m.area_of_circle(num)
print(f"The area of the circle having {radius} is : {area}")