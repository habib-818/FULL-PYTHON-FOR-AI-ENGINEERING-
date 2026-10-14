# Parents class - general animals
class Animal:
    def __init__(self, name):
        self.name = name


    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    

# Child class - specific animals
class Dog(Animal):
    def bark(self):
        return f"{self.name} says wolf"
    

# Create a dog using - Positional arguments
dog_1 = Dog("Buddy")

# Or with named arguments
dog_2 = Dog("Tommy")


# Dog can do animal things (inherited)
print(dog_1.eat())
print(dog_1.sleep())
print(dog_1.bark())