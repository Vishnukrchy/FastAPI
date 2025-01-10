from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Read data from frontend and return it back
# 1) by path variable    
# get by id by passing id as parameter as part of the url or path variable
@app.get("/get-todo/{id}")
def get_todos(id: int):
    print("get-todo is called")
    return "get-todo is called, id: " + str(id)
@app.delete("/delete-todo/{id}")
def delete_todo(id: int):
    print("delete-todo is called")
    return "delete-todo is called, id: " + str(id)
@app.get("/get-todo")
def get_todos(id: int, name: str):
   print("get-todo is called", id, name)
   return {"id": id, "name": name}

student = [{
    "id": 1,
    "name": "John"
}, {
    "id": 2,
    "name": "Doe"
}]
@app.get("/get-student")
def get_student():
    print("get-student is called")
    return student
@app.post("/add-student")
def add_student(id: int, name: str):
    print("add-student is called")
    global student
    student.append({"id": id, "name": name})
    return student  
@app.put("/update-student")
def update_student(id: int, name: str):
  global student
  for s in student:
    if s["id"] == id:
        s["name"]=name
        return student

@app.delete("/delete-student/{id}")
def delete_student(id: int):
    global student
    for s in student:
      if s["id"] == id:
        student.remove(s)
        return student
@app.get("/get-student/{id}")
def get_student_by_id(id: int):
    global student
    for s in student:
       if s["id"]==id:
          return s    
#3) by request body => get by id by passing id as part of the request body => postman => body => raw => json


"""
    This is the main entry point for the todo application.
    It will start the FastAPI application on port 8000
    port  is  8000 and host is 0.0.0.0 to make it accessible from outside the container.

 """
def start():
     uvicorn.run(app, host="127.0.0.1", port=8080)   
