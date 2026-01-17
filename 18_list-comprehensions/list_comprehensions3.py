#list comprehensions = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [ expressions for value in iterable if condition]

grades = [ 85, 42 , 79 , 90 , 56 , 61 , 34]
passing_grades = [ grade for grade in grades if grade >= 60 ]

print(passing_grades)