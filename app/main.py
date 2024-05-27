from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GreetingRequest(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Hello..."}

@app.post("/greet")
def greet(request: GreetingRequest):
    return {"message": f"Hello, {request.name}! \nHave a nice day..."}
