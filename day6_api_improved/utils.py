def predict_with_prob(model, features):
    try:
        probabilities = model.predict_proba([features])[0]
        prediction = model.predict([features])[0]
        return int(prediction), probabilities.tolist()

    except Exception as e:
        return "error", str(e)
