from typing import Any
from pydantic import BaseModel
from datetime import datetime
def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    age: int = 0
    # sum: int = first_name + age
    return full_name

def some_function(data: Any):
    print(data)

def process_items(items: list[ia]):
    for item in items:
        print(item)

class User(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    date_of_birth: datetime | None = None

    def __int__(self):
        return self.id

external_data = {
    "id":1,
    "first_name": "Azeez"
}