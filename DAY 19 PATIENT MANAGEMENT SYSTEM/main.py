import json


from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from fastapi import Path
from fastapi.responses import JSONResponse


from pydantic import BaseModel
from pydantic import Field
from pydantic import computed_field


from typing import Annotated 
from typing import Optional
from typing import Literal


app = FastAPI()

# Main Model

class patient(BaseModel):

    id : Annotated[str , Field(... , description = 'Enter the Id', examples = ['P001' , 'P002'])]
    name : Annotated[str , Field(..., description = 'Enter you name ' , max_length = 50)]
    city : Annotated[str , Field(... , description = 'Enter you City ' , max_length = 25)]
    age : Annotated[int , Field( ... ,description = 'Enter your age' , ge = 0 , le = 120 )]
    gender : Annotated[Literal['male' , 'female' , 'other'] , Field(... ,description = 'Gender of the patient' )]
    height :  Annotated[float , Field(... , description = 'Height of the patient in merters', gt = 0 )]
    weight : Annotated[float , Field(... , description = 'Weight of the patient in kgs', gt = 0 )]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / self.height**2 
        return bmi

    @computed_field
    @property 
    def verdict(self) -> str : 
        if self.bmi <18.5:
            return 'UnderWeight'
        elif self.bmi <25:
            return 'Normal'
        elif self.bmi < 30 :
            return 'Overweight'
        else:
            return 'Obese'

# Update Base Model

class edit_patient(BaseModel):
    name : Annotated[Optional[str] , Field(default = None ,description = 'Enter you name ' , max_length = 50)]
    city : Annotated[Optional[str] , Field(default = None, description = 'Enter you City ' , max_length = 25)]
    age : Annotated[Optional[int] , Field( default = None ,description = 'Enter your age' , ge = 0 , le = 120 )]
    gender : Annotated[Optional[Literal['male' , 'female' , 'other']] , Field(default = None)]
    height :  Annotated[Optional[float] , Field(default = None, description = 'Height of the patient in merters', gt = 0 )]
    weight : Annotated[Optional[float] , Field(default = None , description = 'Weight of the patient in kgs', gt = 0 )]





def load_data():
    with open('patients.json', "r") as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('patients.json' , "w") as f:
        json.dump(data , f)


@app.get("/")
def home():
    return {'Message ' : 'This is a Patient Management System'}


@app.get("/about")
def about():
    return {'Message' : 'It is mainly focus on to help the doctor '}


@app.get("/view")
def view():
    data = load_data()
    return data



@app.get("/patient/{patient_id}")
def Patient(patient_id = Path(... ,description= 'The Id should look like' , example = 'P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404 , detail = 'The Patient ID not found ')



@app.get("/sort")
def sort_order(sort_value :str =Query(... ,description = 'you can also sort this value on the basis of the height , weight , bmi , age' , example='bmi'), order : str = Query('asc' , description = 'you can sorrt the data in a asc , desc order') ):
    valid_field = ["age" , "height" , "weight" , "bmi"]
    if sort_value not in valid_field:
        raise HTTPException(status_code = 400 , detail = f'You can only sort in the basis of a {valid_field}')
    valid_order = ['asc' , 'desc']
    if order not in valid_order:
        raise HTTPException(status_code = 400 , detail = f'you can only take this {valid_order}')
    with open('patients.json' , "r") as f:
        data = json.load(f)
    
    order_func = True if order=='desc' else False

    sorted_data = sorted(data.values() , key=lambda x: x.get(sort_value , 0) , reverse =order_func )

    return sorted_data


@app.post("/create")
def create(cre_patient:patient):
    
    data = load_data() # Step 1 :- Load thre Data 

    if cre_patient.id in data:    # Checking if patient id exit in our database or not 
        raise HTTPException(status_code = 400 , detail = 'patient alredy exit') 
    
    # Making a Conversion of our pydantic model to a Dictonary 

    data[cre_patient.id]  =cre_patient.model_dump(exclude = {'id'})

    # Making a Save to a JSON to a Dictonary 

    save_data(data)

    return JSONResponse(status_code = 201 , content = {'message' : 'patient created sucessfully'})


# Update Endpoint



@app.put("/edit/{patient_id}")
def update_patient(patient_id : str , e_patient:edit_patient ):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code = 404 , detail = 'Patient not found')
    existing_patient_data = data[patient_id]

    update_model_class  =e_patient.model_dump(exclude_unset = True)

    for key , value in update_model_class.items():
        existing_patient_data[key] = value 

    
    existing_patient_data['id'] = patient_id

    existing_patient_class = patient(**existing_patient_data)

    existing_patient_data = existing_patient_class.model_dump(exclude = {'id'})

    data[patient_id]  =existing_patient_data


    save_data(data)

    return JSONResponse(status_code = 200 , content = {"message": "Patient updated successfully"})


# Making a Delete Function 

@app.delete("/delete/{patient_id}")

def delete_patient(patient_id : str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404 , detail = {"message" : "The patient id not found"})
    
    del data[patient_id]

    save_data(data)

    return {"message" : "The patient is deleted"}