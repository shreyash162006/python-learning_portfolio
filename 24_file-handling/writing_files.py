# Python writing files(.txt , .json ,.csv)

txt_data = "i like pizza!"

file_path = "output.txt"
try:
    with open(file_path , mode ="a") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print(" That File already exists!")