# return statement is used to end a function and send a result back to the caller 

'''def add(x , y):
        z = x + y
        return z 

   def substract( x , y):
        z = x - y
        return z

   def multiply( x , y):
        z = x * y
        return z

   def divide( x , y):
        z = x/y
        return z


print(add( 1, 2))
print(substract( 1 ,2 ))
print(multiply( 2, 3))
print(divide( 9 , 3))    '''

def create_name(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("shreyash" , "bokade")
print(full_name)