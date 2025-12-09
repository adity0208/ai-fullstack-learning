from pydantic import BaseModel

class CalculatorRequest(BaseModel):
    a: float
    b: float
