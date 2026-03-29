#exception = An event that interrupts the flow of a program
#           (ZeroDivisionError , TypeError , ValueError)
#           1.try , 2.except , 3.finally

# the user can type in anything
# num = int(input("Enter any number:"))
#print( 1/num )
# if user types 0 it gives ZeroDivisionError
# if user types a string it gives ValueError

try:
    number = int(input("Enter any number : "))
    print( 1 / number )
except ZeroDivisionError:
    print("You cant divide by zero !!")
except ValueError:
    print("Enter only numbers please!!")
except Exception:
    print("Something went wrong !")
finally:                                # it always executes regardless of the presence of exception
    print("Do some cleanup here")