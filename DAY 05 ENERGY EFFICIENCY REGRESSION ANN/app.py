import streamlit as st
import pandas as pd
import numpy as np
import joblib

from keras.models import load_model

scaler = joblib.load('scaling.pkl')

model = load_model('model_energy_ann.keras')

st.title('MACHINE LEARNING MODEL')

Relative_Compactness = st.number_input('Note :- Relative_Compactness' , min_value = 0.0 , max_value = None , step = 0.1)


Surface_Area = st.number_input('Note :- Surface_Area' , min_value = 0.0 , max_value = None , step = 0.1)


Wall_Area = st.number_input('Note :- Wall_Area' , min_value = 0.0 , max_value = None , step = 0.1)


Roof_Area = st.number_input('Note :- Roof_Area' , min_value = 0.0 , max_value = None , step = 0.1)


Overall_Height = st.number_input('Note :- Overall_Height' , min_value = 0.0 , max_value = None , step = 0.1)


Orientation = st.number_input('Note :- Orientation' , min_value = 0.0 , max_value = None , step = 0.1)


Glazing_Area = st.number_input('Note :- Glazing_Area' , min_value = 0.0 , max_value = None , step = 0.1)


Glazing_Area_Distribution = st.number_input('Note :- Glazing_Area_Distribution' , min_value = 0.0 , max_value = None , step = 0.1)


input_data = pd.DataFrame([{
    'Relative_Compactness' : Relative_Compactness , 
    'Surface_Area' : Surface_Area , 
    'Wall_Area' : Wall_Area , 
    'Roof_Area' : Roof_Area , 
    'Overall_Height' : Overall_Height , 
    'Orientation' : Orientation , 
    'Glazing_Area' : Glazing_Area , 
    'Glazing_Area_Distribution'  :  Glazing_Area_Distribution 
}])


input_scaled = scaler.transform(input_data)


if st.button('Predict'):
    
    pred_heat, pred_cool = model.predict(input_scaled)

    heat = np.round(pred_heat[0][0], 0)
    cool = np.round(pred_cool[0][0], 0)

    st.success(
        f'As per the Data the heating load is **{heat}** '
        f'and the cooling load is **{cool}**'
    )