from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("churn_model.pkl")

churn_map = {
    1: "Churn",
    0: "Not Churn"
}

@app.get("/")
def home():
    return {"status": "Churn Prediction API running"}

@app.post("/predict")
def predict(data: dict):
    
    df = pd.DataFrame([data])

    prediction = model.predict(df)

    predicted_class = int(prediction[0])
    predicted_churn = churn_map.get(predicted_class, "Unknown")

    return {
        "predicted_class": predicted_class,
        "predicted_churn": predicted_churn
    }
