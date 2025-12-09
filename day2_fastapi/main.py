from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI project!"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}
