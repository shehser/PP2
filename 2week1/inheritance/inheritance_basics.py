# Parent (Base) Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child (Derived) Class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking: Woof! Woof!")

# Creating an instance of the child class
my_dog = Dog("Rex")

# The child class instance accesses both its own methods and the parent's methods
my_dog.eat()
my_dog.bark()
