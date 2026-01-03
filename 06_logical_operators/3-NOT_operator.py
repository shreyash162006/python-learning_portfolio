#Not = inverts the condition (not False , not True )
user_role = input("Enter your role (admin / user) : ")

if not user_role == "admin" :
    print("Access denied")
else:
    print("Access granted")