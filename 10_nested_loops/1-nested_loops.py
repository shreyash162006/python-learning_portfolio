# nested loop - a loop within another loop (inner , outer)
# the inner loops are executed first and after them the outer loop is executed

#rectangle of stars using nested loops
rows = int(input("Enter the number of rows : "))
coloumns = int(input("Enter the number of coloumns : "))

for x in range(rows):
    for y in range(coloumns):
        print( "*" , end = "")
    print()

