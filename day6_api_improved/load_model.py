import pickle

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print("Error loading model:", e)
    model = None
