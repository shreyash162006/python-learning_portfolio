# iterables = an object /collection that can return its element one at a time , allowing it to be iterated over in a loop

#Iterating lists
numbers  = [ 1 , 2 , 3 , 4 , 5]

for item in reversed(numbers):  #lists are reversible
    print(item , end=" ")
print()
# Iterating tuples
fruits = ( "apple" , "mango" , "banana" , "fig")
for fruit in fruits:
    print(fruit , end=" ")
print() 
for fruit in reversed(fruits): # sets are reversible  
    print(fruit , end =" ")
print()
#Iterating sets ( sets are irreversible) 
#fruits = { "apple" , "mango" , "banana" , "fig" }
#    for fruit in reversed(fruits):
#       print(fruit)

# iterating dictionary
students = { "shreyash" : "science" , "sarvadha" : "commerce" , "vedant" : "arts" , "siddhant" : "architecture"}
for key , value in students.items():
    print(f"{key} : {value}")
    