## TYPE HINTS
"""
 * Normally python lets you to pass any type of data in function.
 * Type Hints explicitly state what type of data the function should recive and return.  
 * FastAPI reads these hints to automatically validate web requests.
 * Standard Python does not inforce strict type it only happens when we have something like pylance, etc

 Example:"""
# The -> str tells us this function returns a string
def greet_user(name:str, age:int) -> str:
    return f"Hello {name}, I'm {age} years old."

greet_user(name="Habib", age=19) # keywrods arguments



## DEFULT ARGUMENTS
"""
 * You can assign a fall back value incase the user does not assign one.
 * These must always go at the end of your parameter list.
 * A non-defult argument (name) can't follow defult argumet (name='Habib')
 
 Example:"""
def fetching_data(endpoint: str, limit: int = 10):
    print(f"Fetching {limit} records to {endpoint}")

fetching_data("/users") # Using the defult limits of 10
fetching_data("/users", 50) # Overrides the default limit to 50



## THE "MUTABLE DEFULT" TRAP
"""
 * Never use a list or dictionary as a default argument.
 * Python evaluates default arguments exactly once when the function is defined, 
   not every time it runs. If you use an empty list [] as a default,
   every single function call shares that exact same list.

 Example: The Bug-"""
def add_item(item: str, my_list: list = []):
    my_list.append(item)
    return my_list

print(add_item("Apple"))  # Output: ['Apple']
print(add_item("Banana")) # Output: ['Apple', 'Banana'] - Wait, Apple is still there!


""" The Fix: Always use None as the default for lists or dictionaries, 
             and create the empty list inside the function.

 Example: """
def add_item(item: str, my_list: list = None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list