# default arguments - a default value for certain parameters. 
#     default is used when that argument is ommited
#         make your function more flexible , reduces , # of arguments
#         1. positional , 2. DEFAULT , 3. keyword , 4. Arbitary


#def net_price( list_price , discount = 0, tax = 0.05):   [ discount and tax have been given default value]
#   return list_price*(1 - discount)*(1 + tax)

#print(net_price(500 , 0.01 ))
#print(net_price(500 , 0.001 , 0.02) )

import time 

def count( end , start= 0):
    for x in range(start , end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10 , 5)