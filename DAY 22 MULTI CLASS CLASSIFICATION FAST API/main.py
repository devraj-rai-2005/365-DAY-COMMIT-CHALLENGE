import joblib
model = joblib.load('cenus_model.pkl')


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'Message : ' : "This is a Home Page of our Model and You can predict the Rich and Poor on the basis of a Income"}

from pydantic import BaseModel , Field
from typing import Annotated ,Literal
import pandas as pd

class validation_model(BaseModel):
    Age :  Annotated[int , Field(... , description = 'Age should be a int')]

    Workclass : Annotated[Literal['State_gov', 'Self_emp_not_inc', 'Private', 'Federal_gov',
       'Local_gov', 'Self_emp_inc', 'Without_pay'] , Field(description = 'We Just want this value of a work class no other value we need')]
    
    fnlwgt : Annotated[float , Field(... , description = 'fnlwgt should be a float')]

    Education : Annotated[Literal['Bachelors', 'HS_grad', '11th', 'Masters', '9th', 'Some_college','Assoc_acdm', '7th_8th', 'Doctorate', 'Assoc_voc', 'Prof_school',
       '5th_6th', '10th', 'Preschool', '12th', '1st_4th'] , Field(description = 'We Just want this value of a Education no other Classes we need')]

    Education_Num  : Annotated[float , Field(... , description = 'Education_Num should be a float')]

    Martial_Status : Annotated[Literal['Never_married', 'Married_civ_spouse', 'Divorced','Married_spouse_absent', 'Separated', 'Married_AF_spouse','Widowed'] , Field(description = 'We Just want this value of a Martial_Status no other Classes we need')]

    Occupation  : Annotated[Literal['Adm_clerical', 'Exec_managerial', 'Handlers_cleaners','Prof_specialty', 'Other_service', 'Sales', 'Transport_moving',
       'Farming_fishing', 'Machine_op_inspct', 'Tech_support','Craft_repair', 'Protective_serv', 'Armed_Forces',
       'Priv_house_serv'] , Field(description = 'We Just want this value of a Occupation no other Classes we need')]

    Relationship  : Annotated[Literal['Not_in_family', 'Husband', 'Wife', 'Own_child', 'Unmarried','Other_relative'] , Field(description = 'We Just want this value of a Relationship no other Classes we need')]

    Race : Annotated[Literal['White', 'Black', 'Asian_Pac_Islander', 'Amer_Indian_Eskimo',
       'Other'] , Field(description = 'We Just want this value of a Race no other Classes we need')]

    Sex  : Annotated[Literal['Male', 'Female'] , Field(description = 'We Just want this value of a Sex no other Classes we need')]

    Capital_Gain : Annotated[float , Field(... , description = 'Capital_Gain should be a float')]

    Capital_Loss :Annotated[float , Field(... , description = 'Capital_Loss should be a float')]

    Hours_per_week  : Annotated[float , Field(... , description = 'Hours_per_week should be a float')]

    Country : Annotated[Literal['United_States', 'Cuba', 'Jamaica', 'India', 'Mexico',
       'Puerto_Rico', 'Honduras', 'England', 'Canada', 'Germany', 'Iran',
       'Philippines', 'Poland', 'Columbia', 'Cambodia', 'Thailand','Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal','Dominican_Republic', 'El_Salvador', 'France', 'Guatemala','Italy', 'China', 'South', 'Japan', 'Yugoslavia', 'Peru',
       'Outlying_US_Guam_USVI_etc', 'Scotland', 'Trinadad_Tobago','Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary',
       'Holand_Netherlands'] , Field(description = 'We Just want this value of a Country no other Classes we need')]
    

@app.post("/predict")

def predict_data(data :validation_model):

    Age = data.Age
    Workclass = data.Workclass
    fnlwgt = data.fnlwgt
    Education = data.Education
    Education_Num = data.Education_Num
    Martial_Status = data.Martial_Status
    Occupation = data.Occupation
    Relationship = data.Relationship
    Race = data.Race 
    Sex = data.Sex 
    Capital_Gain= data.Capital_Gain
    Capital_Loss = data.Capital_Loss
    Hours_per_week = data.Hours_per_week
    Country = data.Country

    input_data = pd.DataFrame([{
        'Age' : Age  ,
        'Workclass': Workclass ,
        'fnlwgt' : fnlwgt  ,
        'Education' : Education , 
        'Education_Num' : Education_Num , 
        'Martial_Status' : Martial_Status , 
        'Occupation' : Occupation , 
        'Relationship' : Relationship , 
        'Race' : Race , 
        'Sex' : Sex ,
        'Capital_Gain' : Capital_Gain , 
        'Capital_Loss' : Capital_Loss, 
        'Hours_per_week' : Hours_per_week , 
        'Country' : Country 
    }])

    predict = model.predict(input_data)[0]

    prediction = {1 : 'Rich' , 0 : 'Poor'}.get(predict)

    return {'Prediction' : prediction}