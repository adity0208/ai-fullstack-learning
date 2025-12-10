from fastapi import FastAPI
from schemas import IrisInput
from load_model import model

app = FastAPI()

@app.post("/predict")
def predict_iris(data: IrisInput):
    features = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    prediction = model.predict(features)[0]
    return {"predicted_class": int(prediction)}
