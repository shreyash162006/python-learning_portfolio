# Python reading files 

import json
file_path = "output.json"

try:
    with open(file_path , "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("Youdo not have access to this file")

    