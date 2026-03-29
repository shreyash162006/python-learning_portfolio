#Python File Handling

import csv
employees = [ ["name" , "age" , "job"],
             ["spongbob" , "20" , "clerk"] ,
             ["patrick" , "21" , "cashier"] ,
             ["neemo" , "30" , "accountant"]
             ]
file_path = "output.txt"

try:
    with open(file_path , "w" , newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path} was created'")
except FileExistsError:
    print("That file alreay exists")
