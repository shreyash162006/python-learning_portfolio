#Python writing files 

import json 

employee = {
    "name" : "Spongbob" ,
    "age" : 30 ,
    "job" : "cook"
}

file_path = "output.txt"

try:
    with open(file_path , "w") as file:
        json.dump(employee , file , indent = 4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!!")