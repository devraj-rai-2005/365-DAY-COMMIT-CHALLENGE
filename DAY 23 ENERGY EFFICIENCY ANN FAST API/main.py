import joblib

scaler = joblib.load('scaler.pkl')

from keras.models import load_model

model = load_model('ee_ann_model.keras')


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {'Message ' : "This is a ANN Model and we ave to make a prediction on a energy efficiency"}


from pydantic import BaseModel , Field
from typing import Annotated
import pandas as pd
import numpy as np


class validation_model(BaseModel):
    
    Relative_Compactness : Annotated[float , Field(... , description = "The Relative_Compactness is having float")] 
     
    Surface_Area  : Annotated[float , Field(... , description = "The Surface_Area is having float")] 

    Wall_Area : Annotated[float , Field(... , description = "The Wall_Area is having float")] 

    Roof_Area  : Annotated[float , Field(... , description = "The Roof_Area is having float")] 

    Overall_Height  : Annotated[float , Field(... , description = "The Overall_Height is having float")] 

    Orientation  : Annotated[float , Field(... , description = "The Orientation is having float")] 

    Glazing_Area  : Annotated[float , Field(... , description = "The Glazing_Area is having float")] 

    Glazing_Area_Distribution  : Annotated[float , Field(... , description = "The Glazing_Area_Distribution is having float")] 


@app.post("/predict")

def value_predict(data : validation_model):

    Relative_Compactness = data.Relative_Compactness
    Surface_Area = data.Surface_Area
    Wall_Area = data.Wall_Area
    Roof_Area = data.Roof_Area
    Overall_Height = data.Overall_Height
    Orientation = data.Orientation
    Glazing_Area = data.Glazing_Area
    Glazing_Area_Distribution = data.Glazing_Area_Distribution

    input_data = pd.DataFrame([{
        'Relative_Compactness' : Relative_Compactness , 
        'Surface_Area' : Surface_Area  , 
        'Wall_Area' : Wall_Area  , 
        'Roof_Area' : Roof_Area  , 
        'Overall_Height' : Overall_Height ,
        'Orientation' : Orientation , 
        'Glazing_Area' : Glazing_Area , 
        'Glazing_Area_Distribution' : Glazing_Area_Distribution
    }])

    scaling_data = scaler.transform(input_data)

    pred_heat, pred_cool = model.predict(scaling_data)

    heat = round(float(pred_heat[0][0]), 2)
    cool = round(float(pred_cool[0][0]), 2)

    return {
    "predictions": {
        "heating_load": heat,
        "cooling_load": cool
    }
}
