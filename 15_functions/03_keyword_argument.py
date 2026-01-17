# keyword argument - an argument preceded by an identifier helps with readability.
# order of  arguments doesnt matter 

def hello(greeting , title , first_name , last_name):
    print(f"{greeting} {title}.{first_name} {last_name}")

# hello("Hello" , "Mr" , "Shreyash" , "Bokade") [ positional arguments]

hello(title = "Mr" , last_name = "Bokade" , first_name="Shreyash" , greeting = "Hello")
#position of arguments doesnt matter as we assign keywords 

#If we are using both keyword and positional arguments we should use the positional arguments according to the position 
hello( "Hello" , last_name = "Bokade" , first_name = "Shreyash" , title = "Mr")