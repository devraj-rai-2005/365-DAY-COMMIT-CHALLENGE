from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model pipeline
model = joblib.load("ames_housing_model.pkl")

@app.get("/")
def home():
    return {"status": "Ames Housing API running"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])
    prediction = model.predict(df)

    return {
        "AMES_HOUSE_PRICE": float(prediction[0])
    }
