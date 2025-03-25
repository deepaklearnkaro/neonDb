from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    surname: str
    age: int
    
    #fast api for neon db
    

people = []

@app.post("/add-person")
def add_person(person: Person):
    people.append(person)
    return {"message": "Person added successfully", "data": person}

@app.get("/people")
def get_people():
    return {"people": people}
