from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model pipeline
model = joblib.load("ee_model.pkl")

@app.get("/")
def home():
    return {"status": "Energy Efficiency API running"}

@app.post("/predict")
def predict(data: dict):

    # Convert input JSON → DataFrame
    df = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(df)

    # Extract both outputs
    heating_load = float(prediction[0][0])
    cooling_load = float(prediction[0][1])

    return {
    "predictions": {
        "heating_load": heating_load,
        "cooling_load": cooling_load
    }
}

