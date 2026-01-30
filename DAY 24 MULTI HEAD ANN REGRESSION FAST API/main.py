from fastapi import FastAPI
import joblib
from keras.models import load_model

scaler = joblib.load('ee_24_scaler.pkl')

model = load_model('24_ee_model.keras')

app = FastAPI()

@app.get("/")

def home():
    return {'Message' :  "The Model is having a Multi Head Regression"}

from pydantic import BaseModel , Field
from typing import Annotated
import pandas as pd


class validate_model(BaseModel):

    Global_active_power : Annotated[float , Field(... , description = 'The values should be in a float')]

    Global_reactive_power : Annotated[float , Field(... , description = 'The values should be in a float')]

    Voltage : Annotated[float , Field(... , description = 'The values should be in a float')]

    Global_intensity : Annotated[float , Field(... , description = 'The values should be in a float')]

    day : Annotated[float , Field(... , description = 'The values should be in a float')]

    month : Annotated[float , Field(... , description = 'The values should be in a float')]

    hour : Annotated[float , Field(... , description = 'The values should be in a float')]

    minute : Annotated[float , Field(... , description = 'The values should be in a float')]


@app.post("/predict")

def predict_model(data : validate_model):

    Global_active_power = data.Global_active_power
    Global_reactive_power = data.Global_reactive_power
    Voltage = data.Voltage
    Global_intensity = data.Global_intensity
    day = data.day
    month = data.month
    hour = data.hour
    minute = data.minute


    input_data = pd.DataFrame([{
        'Global_active_power' : Global_active_power ,
        'Global_reactive_power' : Global_reactive_power , 
        'Voltage' : Voltage , 
        'Global_intensity' : Global_intensity ,
        'day' : day ,  
        'month' : month ,
        'hour' : hour , 
        'minute' :minute 
    }])


    scaled_data = scaler.transform(input_data)

    meter_1 , meter_2 , meter_3 = model.predict(scaled_data)

    m1 = float(round(meter_1[0][0], 0))
    m2 = float(round(meter_2[0][0], 0))
    m3 = float(round(meter_3[0][0], 0))

    return {
        'meter 1' : m1 , 
        'meter 2' : m2 , 
        'meter 3' : m3 , 
    }


