from fastapi import FastAPI, Path
from typing import Optional
from src.student import Student, UpdateStudent, students
app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-students")
async def get_students():
        return {"Data": students}
    
@app.get("/get-student/{student_id}")
async def get_student(student_id: int = Path(..., description="The ID of the student to retrieve", gt=0, lt=100)):
    if student_id in students:
        return students[student_id]
    else:
        return {"error": "Student not found"}

@app.get("/get-by-name")
async def get_student(name: Optional[str] = None):
    for student_id, student in students.items():
        if student["name"].lower() == name:
            return student
    return {"error": "Student not found"}

#combine query and path parameters
@app.get("/get-student-info/{student_id}")
async def get_student_info(student_id: int = Path(..., description="The ID of the student to retrieve", gt=0, lt=100),
                            name: str = None):
    if student_id in students:
        student = students[student_id]
        if name and student["name"].lower() != name.lower():
            return {"error": "Student ID and name do not match"}
        return student
    else:
        return {"error": "Student not found"}


@app.post("/create-student")
async def create_student(student: Student):
    new_id = max(students.keys()) + 1
    students[new_id] = student.model_dump() # this 
    return {"message": "Student created successfully", "student_id": new_id}

@app.put("/update-student/{student_id}")
async def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student not found"}
    student_to_be_updated = students[student_id]
    if student.name != None:
        student_to_be_updated["name"] = student.name

    if student.age != None:
            student_to_be_updated["age"] = student.age
    return {"message": "Student updated successfully", "data": students[student_id]}

@app.delete("/delete-student/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students:
         return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student updated successfully", "data": students}