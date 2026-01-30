from fastapi import FastAPI
import joblib
import pandas as pd


app = FastAPI()

model = joblib.load("electricy_model.pkl")

@app.get("/")

def home():
    return {"status": "Electricity Consumption API running"}
 
@app.post("/predict")

def predict(data: dict):
    
    df = pd.DataFrame([data])
     
    prediction = model.predict(df)
    
    kitchen = float(prediction[0][0])
    
    laundry_room = float(prediction[0][1])
    
    HVAC = float(prediction[0][2])
    
    return {
        
        "predictions": {
            
            "kitchen_load": kitchen,
            
            "laundry_room_load": laundry_room ,
            
            "HVAC_load": HVAC , 
            
            }

}