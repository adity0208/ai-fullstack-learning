from pydantic import BaseModel, Field

class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, description="Length of sepal in cm")
    sepal_width: float = Field(..., gt=0, description="Width of sepal in cm")
    petal_length: float = Field(..., gt=0, description="Length of petal in cm")
    petal_width: float = Field(..., gt=0, description="Width of petal in cm")
