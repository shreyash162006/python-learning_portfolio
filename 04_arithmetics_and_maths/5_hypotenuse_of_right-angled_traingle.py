# To calculate the hypotenuse of a right angles traingle by accepting base and height from the user

import math

base = float(input("Enter the base of traingle : "))
height = float(input("Enter the height of the traingle : "))

#hypotenuse = sqrt(base*base + height*height)
c = (base*base + height*height)

hypotenuse = math.sqrt(c)
print(f"The hypotenuse of a traingle having base {base} cm and height {height} cm is : {hypotenuse}")