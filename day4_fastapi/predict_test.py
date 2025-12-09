import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

sample = [5.1, 3.5, 1.4, 0.2]  # sepal + petal measurements
prediction = model.predict([sample])

print("Predicted class:", prediction[0])
