from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="FastAPI Basic")

class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email: str
    # address: Address
    city: str

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.get("/health")
def health():
    return {"status": "Up and running"}

@app.post("/users")
def get_details(user:User):
    data = {
        "full name": user.name,
        "email": user.email,
        "address": {
            "city": user.city,
        }
    }
    return data

# @app.post("/user")
# def get_details(user:User):
#     return user


if __name__ == "__main__":
    # python -m uvicorn app:app
    uvicorn.run(app, host="0.0.0.0", port=8000) #127.0.0.1