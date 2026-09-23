# FastAPI Student API

This project is a simple FastAPI application for managing student records using an in-memory data store. It is designed as a practical step toward understanding how to build and expose applications and machine learning models through APIs. The project demonstrates CRUD operations using FastAPI, Pydantic models, and Python dictionaries as a temporary in-memory data store.


## Project Overview

The app exposes endpoints to:

- View all students
- Retrieve a single student by ID
- Retrieve a student by name
- Create a new student
- Update an existing student
- Delete a student

The in-memory data is defined in the `src/student.py` module and used by the main API file `main.py`.

## Tech Stack

This project uses the following packages and tools:

- `uv` – Python package manager and project runner
- `fastapi` – Web framework for building the API
- `pydantic` – Data validation and model creation
- `python` – Runtime language for the application
- `typing` – Standard library support for `Optional` and type hints

The main dependencies are defined in `pyproject.toml`:

- `fastapi>=0.141.1`
- `pydantic>=2.13.5`

## Project Structure

```text
fast-api/
├── main.py
├── pyproject.toml
├── README.md
└── src/
    ├── __init__.py
    ├── student.py
    └── user.py
```

### Files

- `main.py` – Main FastAPI application and API routes
- `src/student.py` – Student models and in-memory student data
- `src/user.py` – Additional sample Python/Pydantic examples unrelated to the student API
- `pyproject.toml` – Project metadata and dependency list

## Setup and Installation

This project is configured for use with `uv`.

### 1. Install uv

```bash
pip install uv
```

### 2. Create a virtual environment

```bash
uv venv
e.g uv venv fast-api
```

### 3. Install project dependencies

```bash
uv sync
```

This installs the packages declared in `pyproject.toml`, including FastAPI and Pydantic.

## Running the Application

Start the FastAPI server with uvicorn:

```bash
uv run fastapi dev
```

After starting the application, open:

```text
http://127.0.0.1:8000
```

FastAPI automatically generates interactive API docs here:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Root

```http
GET /
```

Returns a welcome message:

```json
{"message": "Hello World"}
```

### Get all students

```http
GET /get-students
```

Returns all students in the in-memory dictionary.

### Get student by ID

```http
GET /get-student/{student_id}
```

Example:

```http
GET /get-student/1
```

### Get student by name

```http
GET /get-by-name?name=John%20Doe
```

### Get student info using path + query parameters

```http
GET /get-student-info/{student_id}?name=John%20Doe
```

### Create a student

```http
POST /create-student
```

Request body example:

```json
{
  "name": "Emma Wilson",
  "age": 21
}
```

### Update a student

```http
PUT /update-student/{student_id}
```

Request body example:

```json
{
  "name": "Emma Johnson",
  "age": 22
}
```

### Delete a student

```http
DELETE /delete-student/{student_id}
```

## Data Model

The student model is defined with Pydantic in `src/student.py`:

```python
class Student(BaseModel):
    name: str
    age: int
```

Update model:

```python
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
```

These models validate input before processing requests.

## In-Memory Data

The app stores students in a dictionary:

```python
students = {
    1: {"name": "John Doe", "age": 20},
    2: {"name": "Jane Smith", "age": 22},
    3: {"name": "Alice Johnson", "age": 19},
}
```

This data resets when the server restarts because it is not persisted to a database.

## Example with curl

Create a student:

```bash
curl -X POST "http://127.0.0.1:8000/create-student" \
  -H "Content-Type: application/json" \
  -d '{"name":"Emma Wilson","age":21}'
```

Get all students:

```bash
curl "http://127.0.0.1:8000/get-students"
```

## Notes

- This project is a learning/demo API.
- It uses in-memory storage rather than a database.
- The app is designed to be simple and beginner-friendly.
- The `src/user.py` file is not part of the student API logic but shows additional Python and Pydantic usage examples.

## License

This project does not currently include a license file. If needed, add one depending on your intended usage.
