## WHAT IS A CLASS?
"""
 A class is a blueprint for creating objects.
 
  * Attributes: What data the objects stores
  * Methods: What the object can do 
"""

## CLASS VS INSTANCE?
"""
 * Class: The blueprint it's self
 * Instance: The concrete object created from the class.
"""
## CODE
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

jerry = Dog(name="Jerry", breed="Labrador")  # Assining Value to the parameters 
jerry.name   # Calling the parameters by their name