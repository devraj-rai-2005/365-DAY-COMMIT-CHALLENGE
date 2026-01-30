from fastapi import FastAPI

import joblib 

model = joblib.load('iris_model.pkl')

app = FastAPI()

@app.get("/")
def home():
    return {'Message' : "This is a home page of a Iris Model and i am here to assit you for a Iris Model."}

# Making a Pydantic Model that i can validate my model 


from pydantic import BaseModel , Field
from typing import Annotated
import pandas as pd

class validate_model(BaseModel):
    sepal_length : Annotated[float , Field(..., description = 'This is a sepal_length and it should be in a float' , examples = ['5.1' ,'4.7'])]


    sepal_width : Annotated[float , Field(..., description = 'This is a sepal_width and it should be in a float' , examples = ['5.1' ,'4.7'])]


    petal_length : Annotated[float , Field(..., description = 'This is a petal_length and it should be in a float' , examples = ['5.1' ,'4.7'])]


    petal_width : Annotated[float , Field(..., description = 'This is a petal_width and it should be in a float' , examples = ['5.1' ,'4.7'])]


@app.post("/predict")

def get_data(data :validate_model ):

    sepal_length = data.sepal_length
    sepal_width = data.sepal_width
    petal_length = data.petal_length
    petal_width = data.petal_width

    input_data = pd.DataFrame([{
        'sepal_length' : sepal_length , 
        'sepal_width' : sepal_width , 
        'petal_length' : petal_length , 
        'petal_width' : petal_width
    }])


    predict = int(model.predict(input_data)[0])

    map_predict = {0 : 'setosa' , 1 : 'versicolor' , 2 : 'virginica'}.get(predict)

    return { 'Message :': f"The Species class is  {map_predict} "
        ,'Message :': f"The Species type as per dteails is {map_predict} "}