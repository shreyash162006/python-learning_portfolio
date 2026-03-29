#Python file detection

import os
print("Working directory:", os.getcwd())
file_path = r"C:\Users\Shreyash\OneDrive\Desktop\python-learning_portfolio\python-learning_portfolio\24_file-handling\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location does not exist")

