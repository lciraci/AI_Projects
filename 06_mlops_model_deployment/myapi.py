import fastapi
print("FastAPI is imported successfully!")

from fastapi import FastAPI , Path
app = FastAPI()
from typing import Optional

from pydantic import BaseModel

# Define a simple endpoint
# amazon.com/create-user
# GET - Get an information
# POST - Create a new resource
# PUT - Update an existing resource
# DELETE - Delete a resource

# Define a root endpoint

students = {
    1 : {
        "name": "John",
        "age": 20,
        "year": "year 12"
    }
} 

# Index endpoint
@app.get("/")
def index():
    return {"name" : "First data"}

#on command line: python3.11.exe -m uvicorn myapi:app --reload
# on the list http://127.0.0.1:8000/docs to see the API documentation

# Get all students
@app.get("/get/students/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student to retrieve")):
    if student_id in students:
        return students[student_id]
    else:
        return {"error": "Student not found"}
    
# on a web browser, you can access the endpoint like this:
# http://127.0.0.1:8000/get/students/1

#get student by nam
#@app.get("/get-by-name/{student_id}")
#def get_student(*, student_id : int, name : Optional[str] = None, test = int):
#    for student in students.values():
#        if student["name"] == name:
#            return student
#    return {"error": "Student not found with that name"}
#*/

@app.get("/get-by-name")
def get_student(*, name : Optional[str] = None, test = int):
    for student in students.values():
        if student["name"] == name:
            return student
    return {"error": "Student not found with that name"}


# Create a new student
class Student(BaseModel):
    name: str
    age: int
    year: str

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student ID already exists"}
    students[student_id] = student.dict()
    return {"message": "Student created successfully", "student_id": student_id, "student": students[student_id]}


# Update an existing student
@app.put("/update-student/{student_id}")    
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"error": "Student not found"}
    
    if student.name != None:
        students[student_id]["name"] = student.name
    
    if student.age != None:
        students[student_id]["age"] = student.age   

    if student.year != None:
        students[student_id]["year"] = student.year

    return {"message": "Student updated successfully", "student_id": student_id, "student": students[student_id]}