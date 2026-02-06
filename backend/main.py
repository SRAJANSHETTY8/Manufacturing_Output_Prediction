from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

model = pickle.load(open("../model/model.pkl", "rb"))
scaler = pickle.load(open("../model/scaler.pkl", "rb"))
features = pickle.load(open("../model/features.pkl", "rb"))

class InputData(BaseModel):
    data: list[float]

@app.get("/")
def home():
    return {"message": "Manufacturing Output Prediction API"}

@app.post("/predict")
def predict(input: InputData):

    if len(input.data) != len(features):
        return {"error": f"Expected {len(features)} features"}

    arr = np.array(input.data).reshape(1, -1)

    arr = scaler.transform(arr)

    prediction = model.predict(arr)

    return {"prediction": float(prediction[0])}
