from fastapi import FastAPI, Depends
from database import Sessionlocal,engine

from sqlalchemy.orm import Session

from schemas import User
from models import Base,Users

Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    try:
        db=Sessionlocal()
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return {"msg":"Welcome to BE service"}

@app.post('/add_user')
def add_user(user:User,db:Session=Depends(get_db)):
    name=user.name
    email=user.email
    new_user=Users(name=name,email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"User Successfully Added","id":new_user.id}

@app.get('/get_users')
def get_users(db:Session=Depends(get_db)):
    users=db.query(Users).all()
    return users
