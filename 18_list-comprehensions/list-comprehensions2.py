#list comprehensions = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [ expressions for value in iterable if condition]

fruits = [ "apple" , "orange" , "banana" , "coconut"]
fruits_upper = [ fruit.upper() for fruit in fruits ]
print(fruits_upper)
# printing first letter of each item in the list
first = [ fruit[0] for fruit in fruits]
print(first)
# list of numbers 
numbers = [ 1 , -2 , 3 , -4 , 5 , -6 ]

positive_nums= [num for num in numbers if num >= 0 ]
print(positive_nums)

negative_nums= [ num for num in numbers if num <= 0]
print(negative_nums)