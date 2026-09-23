
from typing import Optional
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


#using dictionary of dictionary for mock data
students = {
    1: {"name": "John Doe", "age": 20},
    2: {"name": "Jane Smith", "age": 22},
    3: {"name": "Alice Johnson", "age": 19},
}