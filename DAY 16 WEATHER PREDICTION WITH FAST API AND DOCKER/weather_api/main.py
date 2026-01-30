from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("weather_model.pkl")

# Class mapping
weather_map = {
    2: "rain",
    4: "sun",
    1: "fog",
    0: "drizzle",
    3: "snow"
}

@app.get("/")
def home():
    return {"status": "Weather Classification API running"}

@app.post("/predict")
def predict(data: dict):

    # Convert input to DataFrame
    df = pd.DataFrame([data])

    # Predict class
    prediction = model.predict(df)

    predicted_class = int(prediction[0])
    predicted_weather = weather_map[predicted_class]

    return {
        "predicted_class": predicted_class,
        "predicted_weather": predicted_weather
    }
