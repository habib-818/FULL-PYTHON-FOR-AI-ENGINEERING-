## DECORATORS ( @ )
'''
 -> A decorator takes your function, wraps it in some extra logic, and hands it back.
 -> In Python, you trigger a decorator by placing the @ symbol directly above a function definition.

  Example: 
'''
# The Decorator (The Stunt Double)
def announce_action(func):
    def wrapper():
        print("Action! Rolling cameras...")
        func()  # This executes the original function
        print("Cut! Great take.")
    return wrapper

# The Original Function (The Actor)
@announce_action
def shoot_scene():
    print("Doing the main acting scene.")

shoot_scene()


## USAGE OF FASTAPI
'''
 -> FastAPI gives you pre-built decorators to route web traffic to your functions.
 -> The decorator is the bridge that hooks your Python code up to the actual internet.
 
 Example: 
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/movies")
def get_movies():
    return {"title": "The Matrix", "director": "Wachowskis"}