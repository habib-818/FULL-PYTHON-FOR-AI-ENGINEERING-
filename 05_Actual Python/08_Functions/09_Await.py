# Python Async/Await & FastAPI Concurrency

## The Core Concept
'''
 -> Synchronous (Default): Code runs line by line. If a task takes 10 seconds, the entire program freezes and waits. 

 -> Asynchronous (Concurrent): The program starts a slow task, leaves it running in the background, 
                               and handles other requests in the meantime.

 -> The Mental Model: Instead of staring at a blank wall for 3 hours while the crew builds a living room set (Sync), 
                      you tell them to build it and go shoot a different scene on another stage while you wait (Async).
'''

## The Syntax
'''
1. `async def`: Replaces standard `def`. Declares that a function contains asynchronous operations and is allowed to pause.

2. `await`: Placed directly in front of the slow operation. 
            It tells Python: "Pause this specific function right here until the task finishes, 
            but let the server continue running other code."
'''

## FastAPI Implementation
'''
FastAPI handles asynchronous code natively. Use this pattern whenever your API endpoint needs to do something slow, 
preventing one user's heavy request from freezing the server for everyone else.
'''

import asyncio
from fastapi import FastAPI

app = FastAPI()

# Notice the 'async def' instead of just 'def'
@app.get("/generate-video")
async def create_video():
    print("Starting video generation...")
    
    # 'await' pauses this function, freeing up the server to handle other users!
    # asyncio.sleep(5) simulates a 5-second video rendering process.
    await asyncio.sleep(5) 
    
    return {"message": "Video rendered successfully!"}