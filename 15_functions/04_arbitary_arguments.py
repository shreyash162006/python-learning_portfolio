#  *args = allows you to pass multiple non-key arguments
# **kwargs** = allows you to pass multiple keyword-arguments
#         *unpacking operator

'''def add( a , b):
    return a + b
print(add( 1 ,2 , 4 ))'''  # error as we have 2 arguments (a , b)but gave 3 inputs (1,2,4) 

def hello(*args):
    print(type(args)) 
hello()
# the *args stores the arguments in a tuple and the tuple methods can be used to access the arguments

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add( 1,2,3,4,5,6))
# the ** method stores all the arguments into a dictionary and they can be accessed using the dict methods
def print_address(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f" {key} : {value} ")

print_address( street ="ABD Lane" , city ="Mumbai" , state ="Maharashtra" , zip ="411000" ,)

# using them together 
def shipping_label( *args , **kwargs):
    for arg in args:
        print(arg , end=" ")
    for key ,value in kwargs.items():
        print(f" {key} : {value}")
shipping_label("Dr" , "Spongebob" , "Squarepants" , "111",
               street = "MG Road" , apt = "100" , city = "Nagpur" , state = "Maharashtra" , zip = "4101010")
