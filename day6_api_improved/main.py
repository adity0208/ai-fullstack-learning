from fastapi import FastAPI, HTTPException
from schemas import IrisInput
from load_model import model
from utils import predict_with_prob

app = FastAPI(title="Improved Iris ML API", version="2.0")

@app.post("/predict")
def predict_iris(data: IrisInput):

    if model is None:
        raise HTTPException(status_code=500, detail="Model not available")

    features = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]

    pred_class, probabilities = predict_with_prob(model, features)

    if pred_class == "error":
        raise HTTPException(status_code=400, detail=probabilities)

    return {
        "predicted_class": pred_class,
        "confidence_scores": probabilities
    }
