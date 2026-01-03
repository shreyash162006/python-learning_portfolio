#OR operator - at least one condition should be true
#Entry permission program
age = int(input("Enter your age : "))
has_pass = input("Do you have an entry pass ?[yes / no] ")

if(age >= 18 or has_pass == "yes"):
    print("Entry allowed")
else:
    print("Entry not allowed")
    