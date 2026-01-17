# function - a block of reusable code
#        place () after the function name 

''' def greet() :
        print(f"Good morning , {name}")
    name = input("Enter your name :")
    greet()                                            '''

# Arguments
'''def greet(name) :
    print(f"Good morning ,{name}")
greet("shreyash")'''   

def display_invoice( username , amount , due_date ):
    print(f"Hello , {username}")
    print(f"Your bill of ₹{amount : 2f} is due : {due_date}")

display_invoice("BroCode" , 500 , "31/01/2026")