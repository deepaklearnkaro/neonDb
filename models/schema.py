from pydantic import BaseModel

class PersonCreate(BaseModel):
    name: str
    surname: str
    age: int

    class Config:
        from_attributes = True  # Correct way to use Pydantic ORM mode
