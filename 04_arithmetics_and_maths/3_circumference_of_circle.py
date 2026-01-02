# To accept the radius from user and calculate the circumference of circle

import math

radius = float(input("Enter the radius of circle : "))

# formula - circumference = 2*(pie)*radius
circumference = 2*(math.pi)*(radius)

print(f"The circumference of a circle having radius (radius)cm is : {circumference}cm")