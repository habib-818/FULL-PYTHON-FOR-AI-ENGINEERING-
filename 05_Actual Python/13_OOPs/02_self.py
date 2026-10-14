## WHAT IS SELF?
"""
 'self' refers to the current object. 
 It's how an object keeps track of it's data.
"""

class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Bro cat")
dog1.name

dog2 = Dog("Tommy")
dog2.name
