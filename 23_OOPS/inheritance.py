#Inheritane = Allows a class to inhert attribute and methods from another class 
#             Helps with code reusability and extensibility
#             class child(parent)

class animal:        #parent class
    def __init__(self , name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(animal):      #child class
    pass

class Cat(animal):            #child class
    pass

class Mouse(animal):             #child class
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(cat.name)
print(mouse.is_alive)
cat.eat()
mouse.sleep()
