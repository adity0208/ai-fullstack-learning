from fastapi import FastAPI
from schemas import CalculatorRequest

app = FastAPI()

@app.post("/calculate")
def calculate(data: CalculatorRequest):
    result = {
        "add": data.a + data.b,
        "subtract": data.a - data.b,
        "multiply": data.a * data.b,
        "divide": data.a / data.b if data.b != 0 else "undefined"
    }
    return result
