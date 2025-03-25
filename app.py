from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import models
from models.schema import PersonCreate  # Import Pydantic schema

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add-person")
def add_person(person: PersonCreate, db: Session = Depends(get_db)): 
    new_person = models.Person(**person.model_dump())  
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return {"message": "Person added successfully", "data": new_person}

@app.get("/people")
def get_people(db: Session = Depends(get_db)):
    people = db.query(models.Person).all()
    return {"people": people}
