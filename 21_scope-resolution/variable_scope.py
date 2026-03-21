# variable scope = where a variable is visible and accessible is called its scope 
# scope resolution - {LEGB} Local - > Enclosed -> Global -> Built-in

#local variable 
def fun1():
    a = 1    # a can be used only within fun1()
    print(a)
fun1()

# Built-in 
from math import e 
 
def built_in():
    print(e)
built_in()

# gloabal variable 
g = 30    # X can be used anywhere in this program file
def global_var():
    print(g)
global_var()

#enclosed , local , global example
x = "global variable"  # x is a global variable 

def outer():
    y = "enclosed variable"  # enclosed ( non - local )
    def inner():
        z= "local varibale"  # local variable 
        print(z)
        print(y)
        print(x)
    
    inner()
outer()