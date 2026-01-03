# to check the number entered by the user lies between 1 -10

num = int(input("Enter any number [from 1-10 ]: "))

while( num < 1 and num > 10 ):
    print(f"{num} is not valid")
    num = int(input("Enter any number [from 1-10 ]: "))

print(f"Your number is : {num}") 