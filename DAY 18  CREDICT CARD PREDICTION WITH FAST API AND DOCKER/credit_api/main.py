from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("credit_model.pkl")

churn_map = {
    1: "Credict Fraud Found",
    0: "No Credict Fraud Found"
}

@app.get("/")
def home():
    return {"status": "Churn Prediction API running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    Prediction = model.predict(df)
    
    predicted_class = int(Prediction[0])
    predicted_churn = churn_map.get(predicted_class, "Unknown")
    
    return {
        "predicted_class": predicted_class,
        "predicted_churn": predicted_churn
        
        }