# Static method -  a method that belongs to a class rather than any object from that class(instance)
#                  Usually used for general utility functions

# Instance methods - best for operations of the class(objects)
# Static methods - Best for utility functions that do not need access to class data.

class Employee:

    def __init__(self , name , position):
        self.name = name
        self.position = position
    # instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod              #static method
    def is_valid_position(position):
        valid_position = ["Manager" , "cashier" , "Cook" , "Janitor"]
        return position in valid_position
    
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Engineer"))

employee1 = Employee("Henry" , "Cook")
employee2 = Employee("Mark" , "Cashier")
print(employee1.get_info())
print(employee2.get_info())
