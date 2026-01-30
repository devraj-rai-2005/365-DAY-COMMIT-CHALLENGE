from fastapi import FastAPI

import joblib

model = joblib.load('ee_model.pkl')

app = FastAPI()

@app.get("/")
def home():
    return {'Message' : "This is a Multi Label Regression Problem "}




# Making a pydantic model for a vaidation
import pandas as pd
from pydantic import BaseModel , Field
from typing import Annotated 

class checking_model(BaseModel):
    Relative_Compactness : Annotated[float , Field(...,ge = 0)]
    Surface_Area : Annotated[float , Field(...,ge = 0,)]
    Wall_Area :Annotated[float , Field(...,ge = 0,)]
    Roof_Area : Annotated[float , Field(...,ge = 0,)]
    Overall_Height : Annotated[float , Field(...,ge = 0,)]
    Orientation : Annotated[float , Field(...,ge = 0,)]
    Glazing_Area : Annotated[float , Field(...,ge = 0,)]
    Glazing_Area_Distribution  : Annotated[float , Field(...,ge = 0,)]


@app.post("/predict")
def model_predict(data :checking_model ):
    Relative_Compactness = data.Relative_Compactness
    Surface_Area = data.Surface_Area
    Wall_Area = data.Wall_Area
    Roof_Area = data.Roof_Area
    Overall_Height = data.Overall_Height
    Orientation = data.Orientation
    Glazing_Area = data.Glazing_Area
    Glazing_Area_Distribution = data.Glazing_Area_Distribution


    input_data = pd.DataFrame([{
        'Relative_Compactness' : Relative_Compactness,
        'Surface_Area' : Surface_Area ,  
        'Wall_Area' : Wall_Area   , 
        'Roof_Area' : Roof_Area  , 
        'Overall_Height' : Overall_Height  , 
        'Orientation' : Orientation , 
        'Glazing_Area' : Glazing_Area , 
        'Glazing_Area_Distribution' : Glazing_Area_Distribution 
    }])

    predict = model.predict(input_data)[0]

    heating_load = float(round(predict[0],0))
    cooling_load = float(round(predict[1],1))

    return {
    "heating_load": heating_load,
    "cooling_load": cooling_load
}
