# Built-in math functions in python

x = 3.142
y = -4
z = 5
print(f" X = {x}")
print(f" Y = {y}")
print(f" Z = {z}")
# 1. round function - returns nearest whole number 
round = round(x)
print(f"The rounded digit for X is : {round}")

# absolute value - abs()
absolute = abs(y)
print(f"The absolute value for Y is : {absolute}")

#pow(base , exponent)- returns base raised to exponent 
power = pow( 5 , 2 )
print(f"{z} to the power 2 is : {power}")

#max() - returns maximum value
max = max(x , y , z)
print(f"The maximum value between {x} , {y} and {z} is : {max}")

#min() - returns minimum value 
min = min(x , y , z)
print(f"The minimum value between {x} , {y} and {z} is : {min}")

#importing math library
import math
print("The value of pie is : ",end=" ")
print(math.pi)
e = math.e
print(f"The value of e is : {e}")
# square root of a number 
num = 25
square_root = math.sqrt(num)
print(f"The sqaure root of {num} is : {square_root} " )

# math.ceil()- rounds up a number
digit = 9.56
round_up = math.ceil(digit)
print(f"The rounded up number for {digit} is : {round_up}")

#math.floor - rounds down a number
round_down = math.floor(digit)
print(f"The rounded down number for {digit} is : {round_down}")
