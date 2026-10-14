## WHAT IS PARAMETER AND ARGUMENTS?
"""
 * Parameter = the variable name listed in the function's definition. It's a placeholder.
 * Argument = the actual value you pass in when you call the function.
"""
def greet(name, age):   # `name` and `age` are PARAMETERS
    print(f"{name} is {age} years old")

greet("Habibur", 19)    # "Habibur" and 19 are ARGUMENTS

greet(name="Habib", age=18) # This are keyword-arguments