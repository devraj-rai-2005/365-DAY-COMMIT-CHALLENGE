import joblib
import numpy as np
import streamlit as st 
import pandas as pd

model = joblib.load('uci_classification_model.pkl')


st.title('UCI CREDIT CARD DETETCION')
st.header('MACHINE LEARNING MODEL OF CLASSIFICATION')
st.divider()

st.subheader('FILL THE INPUTS AND CHECK THE DEFAULTER')


LIMIT_BAL = st.number_input('Note :- LIMIT_BAL' , min_value =0 , step = 1 , max_value =None)


SEX = st.selectbox('Note :- SEX', ['F' , 'M'])

EDUCATION = st.selectbox('Note :- EDUCATION', ['University' , 'Graduate_school' ,  'High_School' , 'Unknown' ,'Others' , 'No_Education'  ])


MARRIAGE = st.selectbox('Note :- MARRIAGE', ['Single' , 'Married' , 'Other' , 'Unknown'])


AGE = st.number_input('Note :- AGE' , min_value =0 , step = 1 , max_value =None)


PAY_0 = st.number_input('Note :- PAY_0' , min_value =0 , step = 1 , max_value =None)


PAY_2 = st.number_input('Note :- PAY_2' , min_value =0 , step = 1 , max_value =None)


PAY_3 = st.number_input('Note :- PAY_3' , min_value =0 , step = 1 , max_value =None)


PAY_4 = st.number_input('Note :- PAY_4' , min_value =0 , step = 1 , max_value =None)


PAY_5 = st.number_input('Note :- PAY_5' , min_value =0 , step = 1 , max_value =None)


PAY_6 = st.number_input('Note :- PAY_6' , min_value =0 , step = 1 , max_value =None)


BILL_AMT1 = st.number_input('Note :- BILL_AMT1' , min_value =0 , step = 1 , max_value =None)


BILL_AMT2 = st.number_input('Note :- BILL_AMT2' , min_value =0 , step = 1 , max_value =None)


BILL_AMT3 = st.number_input('Note :- BILL_AMT3' , min_value =0 , step = 1 , max_value =None)


BILL_AMT4 = st.number_input('Note :- BILL_AMT4' , min_value =0 , step = 1 , max_value =None)


BILL_AMT5 = st.number_input('Note :- BILL_AMT5' , min_value =0 , step = 1 , max_value =None)


BILL_AMT6 = st.number_input('Note :- BILL_AMT6' , min_value =0 , step = 1 , max_value =None)


PAY_AMT1 = st.number_input('Note :- PAY_AMT1' , min_value =0 , step = 1 , max_value =None)


PAY_AMT2 = st.number_input('Note :- PAY_AMT2' , min_value =0 , step = 1 , max_value =None)


PAY_AMT3 = st.number_input('Note :- PAY_AMT3' , min_value =0 , step = 1 , max_value =None)


PAY_AMT4 = st.number_input('Note :- PAY_AMT4' , min_value =0 , step = 1 , max_value =None)


PAY_AMT5 = st.number_input('Note :- PAY_AMT5' , min_value =0 , step = 1 , max_value =None)


PAY_AMT6 = st.number_input('Note :- PAY_AMT6' , min_value =0 , step = 1 , max_value =None)


input_data = pd.DataFrame([{
    'LIMIT_BAL' : LIMIT_BAL, 
    'SEX' : SEX, 
    'EDUCATION' : EDUCATION, 
    'MARRIAGE' : MARRIAGE , 
    'AGE' : AGE , 
    'PAY_0' : PAY_0 , 
    'PAY_2' : PAY_2 , 
    'PAY_3' : PAY_3 , 
    'PAY_4' : PAY_4 , 
    'PAY_5' : PAY_5, 
    'PAY_6' : PAY_6, 
    'BILL_AMT1' : BILL_AMT1   , 
    'BILL_AMT2' : BILL_AMT2  , 
    'BILL_AMT3' : BILL_AMT3 , 
    'BILL_AMT4' : BILL_AMT4 , 
    'BILL_AMT5' : BILL_AMT5 , 
    'BILL_AMT6' : BILL_AMT6 , 
    'PAY_AMT1' : PAY_AMT1 , 
    'PAY_AMT2' : PAY_AMT2 , 
    'PAY_AMT3' : PAY_AMT3 , 
    'PAY_AMT4' : PAY_AMT4, 
    'PAY_AMT5' : PAY_AMT5 , 
    'PAY_AMT6' : PAY_AMT6 , 
}])


if st.button('Predict'):
    
    predict = model.predict(input_data)[0]
    
    prediction = {1 : 'Yes you are in a Defaulter'  , 0 : 'No you are not in a Defaulter'}.get(predict)
    
    st.success(f'The Approximate Prediction for a credict card is **{prediction}**')