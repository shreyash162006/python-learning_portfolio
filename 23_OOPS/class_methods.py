#class methods - Allows operation related to class itself
#                Take {cls} as the first parameter , which represents the class itself 

class Student:

    count = 0
    total_gpa = 0

    def __init__(self , name , gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instnace method
    def get_info(self):
        return f"{self.name} scored {self.gpa} cgpa"
        
    @classmethod
    def get_count(cls):
        return f"Total number of students :{cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0 
        else:
            return f"{cls.total_gpa / cls.count}"
    
print(Student.get_count())
student1 = Student("Shreyash", 8.7)
student2 = Student("Om" , 8.5)
student3 = Student("Sahil" , 8.45)
print(Student.get_count())
print(Student.get_avg_gpa())