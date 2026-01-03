#Logical operators - evaluate multliple conditions (or , and , not ) 
#                   or = at least one condition should be true
#                   and = both conditions must be true
#                   not = inverts the condition (not False , not True )

# And operator- Program to find greatest of three numbers
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
num3 = float(input("Enter the third number : "))
 
if( num1>num2 and num1>num3):
    print(f"{num1} is the greatest among the three")
elif( num2>num1 and num2>num3 ):
    print(f"{num2} is the greatest among the three ")
else:
    print(f"{num3} is the greatest among the three ")
