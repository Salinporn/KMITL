from fastapi import FastAPI
from fastapi import Request
from fastapi import Body

app = FastAPI()

students = {
    29 : {"ID": 29, "first_name": "Kazuha", "last_name": "Kaedehara"},
    30 : {"ID": 30, "first_name": "Albedo", "last_name": "Rhinedottir"},
}

@app.get("/path/path_parameter")
async def funtion_name(path_parameter: str):
    # add code here
    return {"path_parameter": path_parameter}

@app.get("/students/all")
async def get_students():
    return students

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    return students[student_id]

@app.post("/students/new/")
async def create_student(student: dict = Body(...)):
    if student["ID"] in students:
        return {"error": "Student already exists"}
    student_id = max(students.keys()) + 1  
    students[student_id] = student
    return students

@app.post("/students/new/{first_name}/{last_name}/{student_id}")
async def create_student(first_name: str, last_name: str, student_id: int):
    if student_id in students:
        return {"error": "Student already exists"}
    student = {"ID": student_id, "first_name": first_name, "last_name": last_name}
    students[student_id] = student
    return students

@app.post("/students/newForm")
async def create_student_form(student_id: int, first_name: str, last_name: str):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = {"ID": student_id, "first_name": first_name, "last_name": last_name}
    return students[student_id]
