import streamlit as st
import pandas as pd
import joblib 
import numpy as np

from keras.models import load_model

model = load_model('Adult_Census.keras')

ordinal = joblib.load('ordinal_encoder.pkl')

scaler = joblib.load('scaler.pkl')


st.title('MACHINE LEARNING MODEL')


Age = st.number_input('Note :- Age' , min_value = 0 , step = 1 , max_value = None)


Workclass= st.selectbox('Note :- Workclass' , [" Private", " Self_emp_not_inc", " Local_gov", " State_gov", " Self_emp_inc", " Federal_gov", " Without_pay"])


fnlwgt= st.number_input('Note :- fnlwgt' , min_value = 0.0 , step = 1.0 , max_value = None)


Education= st.selectbox('Note :- Education' , [" HS_grad", " Some_college", " Bachelors", " Masters", " Assoc_voc", " 11th", " Assoc_acdm", " 10th", " 7th_8th", " Prof_school", " 9th", " 12th", " Doctorate", " 5th_6th", " 1st_4th", " Preschool"])


Education_Num = st.number_input('Note :- Education_Num' , min_value = 0.0 , step = 1.0 , max_value = None)


Martial_Status= st.selectbox('Note :- Martial_Status' , [" Married_civ_spouse", " Never_married", " Divorced", " Separated", " Widowed", " Married_spouse_absent", " Married_AF_spouse"])


Occupation= st.selectbox('Note :- Occupation' , [" Prof_specialty", " Craft_repair", " Exec_managerial", " Adm_clerical", " Sales", " Other_service", " Machine_op_inspct", " Transport_moving", " Handlers_cleaners", " Farming_fishing", " Tech_support", " Protective_serv", " Priv_house_serv", " Armed_Forces"])


Relationship= st.selectbox('Note :- Relationship' , [" Husband", " Not_in_family", " Own_child", " Unmarried", " Wife", " Other_relative"])


Race= st.selectbox('Note :- Race' , [" White", " Black", " Asian_Pac_Islander", " Amer_Indian_Eskimo", " Other"])


Sex= st.selectbox('Note :- Sex' , [" Male", " Female"])


Capital_Gain = st.number_input('Note :- Capital_Gain' , min_value = 0.0 , step = 1.0 , max_value = None)


Capital_Loss = st.number_input('Note :- Capital_Loss' , min_value = 0.0 , step = 1.0 , max_value = None)


Hours_per_week = st.number_input('Note :- Hours_per_week' , min_value = 0, step = 1 , max_value = None)


Country= st.selectbox('Note :- Country' , [" United_States", " Mexico", " Philippines", " Germany", " Puerto_Rico", " Canada", " El_Salvador", " India", " Cuba", " England", " Jamaica", " South", " Italy", " China", " Dominican_Republic", " Vietnam", " Guatemala", " Japan", " Columbia", " Poland", " Haiti", " Iran", " Taiwan", " Portugal", " Nicaragua", " Peru", " Greece", " France", " Ecuador", " Ireland", " Hong", " Trinadad_Tobago", " Cambodia", " Laos", " Thailand", " Yugoslavia", " Outlying_US_Guam_USVI_etc", " Hungary", " Honduras", " Scotland", " Holand_Netherlands"])


input_data = pd.DataFrame([{
    'Age' : Age  , 
    'Workclass' : Workclass , 
    'fnlwgt' : fnlwgt , 
    'Education' : Education , 
    'Education_Num' : Education_Num , 
    'Martial_Status' : Martial_Status  , 
    'Occupation' : Occupation , 
    'Relationship' : Relationship , 
    'Race' : Race  , 
    'Sex' : Sex , 
    'Capital_Gain' : Capital_Gain , 
    'Capital_Loss' : Capital_Loss , 
    'Hours_per_week' : Hours_per_week , 
    'Country' : Country
}])


cat_cols = [
    'Workclass','Education','Martial_Status',
    'Occupation','Relationship','Race','Sex','Country'
]


cat_cols = [
    'Workclass','Education','Martial_Status',
    'Occupation','Relationship','Race','Sex','Country'
]

num_cols = [
    'Age','fnlwgt','Education_Num',
    'Capital_Gain','Capital_Loss','Hours_per_week'
]

# Encode categorical
input_data[cat_cols] = ordinal.transform(input_data[cat_cols])


# Scale numerical
input_data[num_cols] = scaler.transform(input_data[num_cols])



if st.button("Predict"):

    y_prob = model.predict(input_data)[0][0]   # probability value
    
    pred_class = int(y_prob >= 0.5)

    label_map = {0: 'Less', 1: 'More'}

    st.success(f"The Adult Census income is **{label_map[pred_class]}** than 50K USD**")

