#list comprehensions = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [ expressions for value in iterable if condition]

# tradational way 
'''doubles = [ ]
for x in range( 1 , 11):
    doubles.append(x * 2)
print(doubles)'''

#[ expressions for value in iterable if condition]
# Here , expression = x*2 , value = x , iterable = range (1 ,11)

doubles =[ x*2 for x in range( 1 , 11)]   # do not use ( : )  in the for loop it gives error
print(doubles)
triples = [ y * 3 for y in range( 1 , 11)]
print(triples)

squares  = [ x *x for x in range(1 , 11)]
print("The square of numbers from 1 - 10 is :")
print()
print(squares)