#"Duck typing" = Another way to achieve polymorphism besides Inheritence 
#                Object must have the minimum necessary attributes/ methods
#               "If it looks like a duck and quacks like a duck , It must be duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!!")

class Cat(Animal):
    def speak(self):
        print("MEOW!!")

class Cars:               # it has the attributes and methods like animals so it can be considered a animal
    
    alive = False

    def speak(self):
        print("HONK!!")

animals = [ Dog() , Cat() , Cars()]

for animal in animals :
    animal.speak()
    print(animal.alive)