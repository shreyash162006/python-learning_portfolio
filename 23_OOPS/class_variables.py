# class variables = Shared amonmg all instances of a class
#                   Defined outside the constructor
#                   allow you to share data among all objects created from that class

class student:

    class_year = 2024  # class variables
    num_students = 0

    def __init__(self , name , age):
        self.name = name  #instance variables
        self.age = age
        student.num_students += 1

student1 = student("Shreyash" , 20)
student2 = student("Siddhant" , 19)
student3 = student("Krrish" , 21)

print(f"My graduating class of {student.class_year} has {student.num_students}")