#magic methods = Dunder methods(double underscore) __init__() , __str__ , __eq__
#                They are automatically called by many of Pythons built-in operations.
#                They allow developers to define or customize the behavior of objects.

class Book:
    
    def __init__(self , title , author , num_pages):
        self.title = title 
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' , {self.author}"
    
    def ___eq__(self , other):
        return self.title == other.title and self.author == other.author
    
    def __gt__(self, other):
        # Greater than: compare by number of pages
        return self.num_pages > other.num_pages
        
book1 = Book("The Hobbit" , "J.R.R" , 310)
book2 = Book("Mindset" , "C.S Dwek" , 264)
book3 = Book("The lion , the witch and the wardrobe" , "C.S Lewis" , 172)
print(book1)
print(book2)
print(book3)

print(book1 == book2)  # True if book 1 and book2 have same title , author and num of pages
print(book2 > book3)