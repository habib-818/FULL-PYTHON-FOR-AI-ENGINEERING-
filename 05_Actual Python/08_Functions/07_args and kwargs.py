## *args & **kwargs
'''
 -> Here the magic is done by it's asterisks (* & **)
 -> This things solve the problem, how do you write a function 
    when you don't know how many arguments the user is going to pass? 
'''


## *args
'''
 -> The single asterisk * gathers multiple positional arguments and packs them into a Tuple.
 -> Just remember * means "take all these unnamed inputs and put them in a tuple."
 
 Example:
'''
def multiply_everything(*args):
    # Inside the function, 'args' is just a normal tuple: (2, 4, 5)
    result = 1
    for number in args:
        result = result * number
    return result

# You can pass as many arguments as you want
print(multiply_everything(2, 4))       # Output: 8
print(multiply_everything(2, 4, 5, 10)) # Output: 400


## **kwrgs
'''
 -> The double asterisk ** gathers named arguments (where you use an equals sign) and packs them into a Dictionary.
 -> Just remember ** means "take all these named inputs and put them in a dictionary."
 
 Example:
'''
def configure_model(**kwargs):
    # Inside the function, 'kwargs' is a dictionary: {'epochs': 10, 'learning_rate': 0.01}
    for key, value in kwargs.items():
        print(f"Setting {key} to {value}")

# You name the arguments right inside the function call
configure_model(epochs=10, learning_rate=0.01, use_gpu=True)


## COMBINING THEM THOGHETER
'''
 -> The strict syntax rule is they must go in this exact order: standard arguments first, then *args, then **kwargs.

 Example: 
'''
def train_model(model_name, *args, **kwargs):
    print(f"Training {model_name}")
    print(f"Extra data passed: {args}")
    print(f"Configuration: {kwargs}")

train_model("RandomForest", 100, 200, max_depth=5, random_state=42)