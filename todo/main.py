from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-todos")  
def get_todos():
    print("get-todos is called")
    return "get-todos is called"

@app.post("/add-todo")
def add_todo():
    print("add-todo is called")
    return "add-todo is called"

@app.put("/update-todo")
def update_todo():
    print("update-todo is called")
    return "update-todo is called"  
    



"""
    This is the main entry point for the todo application.
    It will start the FastAPI application on port 8000
    port  is  8000 and host is 0.0.0.0 to make it accessible from outside the container.

 """
def start():
     uvicorn.run(app, host="127.0.0.1", port=8080)   
