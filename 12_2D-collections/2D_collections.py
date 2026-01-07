# 2D lists
# A 2D list is a list made up of two or more lists
# 2D-list = [ list1 , list2 , list3 ]

fruits = [ "mango" , "apple" , "guava" , "pineapple" ]
vegetables = [ "potato" , "brinjal" , "cabbage" , "letius" ]
dairy_products = [ "milk" , "curd" , "paneer" , "butter" ]

groceries = [ fruits , vegetables , dairy_products ]
print(groceries)

#slicing 2D lists
print(groceries[0])  # prints first list that is fruits 
print(groceries[2])  # prints third list (dairy_products)

# To print element of a list in a 2D list 

print(groceries[1][0])  # prints element at index zero from vegetables
print(groceries[2][3])