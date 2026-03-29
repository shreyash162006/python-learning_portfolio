# multiple inheritance = inhert from more than one parent class 
#                         C(A , B)

# multi-level inheritance = inhert from a parent which inherts from another  parent 
#                          C(B) <-  B(A) <- A

class Animal:
    def __init__(self , name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")
        
    def sleep(self):
        print(f"This {self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey , Predator):
    pass

rabbit = Rabbit("Joe")
hawk = Hawk("Hawk")
fish = Fish("Goldie")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

#rabbit.hunt()        #gives an error
fish.eat()
hawk.sleep()
