# While loop = execute some code while a condition is true 

age= int(input("Enter your age : "))

while age < 0 : 
    print("Age cannot be negative  ")
    age= int(input("Enter your age : "))

print(f"You are {age} years old ")
