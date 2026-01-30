import numpy as np
import pandas as pd
import joblib
import streamlit as st


model = joblib.load('ames_housing_regression_model.pkl')


st.title('AMES HOUSING PREDICTION')
st.header('It is a Machine Learning model that predict the ames house price.')

st.divider()

st.subheader('Fill the Inputs and get a Approximate House Value in the Area')

st.divider()

Overall_Qual = st.number_input('Note :- Overall_Qual' ,  min_value = 0 , max_value = None , step = 1)


Year_Built = st.number_input('Note :- Year_Built' , min_value = 1800 , max_value = None , step = 1 )


Year_Remod_Add = st.number_input('Note :- Year_Remod_Add' , min_value = 1800 , max_value = None , step = 1 )


Mas_Vnr_Area = st.number_input('Note :- Mas_Vnr_Area' , min_value = 0.0 , max_value = None , step =0.1 )


Exter_Qual  = st.selectbox('Note :- Exter_Qual ', [ 'TA' , 'Gd' , 'Ex' , 'Fa'  ])


Bsmt_Qual  = st.selectbox('Note :- Bsmt_Qual ', [ 'TA' , 'Gd' , 'Ex' , 'Fa' , 'Unknown' , 'Po'  ])


BsmtFin_SF_1 = st.number_input('Note :- BsmtFin_SF_1' , min_value = 0.0 , max_value = None , step =0.1 )


Total_Bsmt_SF = st.number_input('Note :- Total_Bsmt_SF' , min_value = 0.0 , max_value = None , step =0.1 )


Heating_QC  = st.selectbox('Note :- Heating_QC ', [ 'TA' , 'Gd' , 'Ex' , 'Fa' , 'Po'  ])



first_Flr_SF = st.number_input('Note :- 1st_Flr_SF' , min_value = 0.0 , max_value = None , step =0.1 )


Gr_Liv_Area = st.number_input('Note :- Gr_Liv_Area' , min_value = 0.0 , max_value = None , step =0.1 )



Full_Bath = st.number_input('Note :- Full_Bath' , min_value = 0.0 , max_value = None , step =0.1 )



Kitchen_Qual  = st.selectbox('Note :- Kitchen_Qual ', [ 'TA' , 'Gd' , 'Ex' , 'Fa' , 'Po'  ])


TotRms_AbvGrd = st.number_input('Note :- TotRms_AbvGrd' , min_value = 0.0 , max_value = None , step =0.1 )


Fireplaces = st.number_input('Note :- Fireplaces' , min_value = 0.0 , max_value = None , step =0.1 )



Fireplace_Qu  = st.selectbox('Note :- Fireplace_Qu ', ['Unknown', 'TA' , 'Gd' , 'Ex' , 'Fa' , 'Po'  ])


Garage_Yr_Blt = st.number_input('Note :- Garage_Yr_Blt' , min_value = 0.0 , max_value = None , step =0.1 )


Garage_Finish  = st.selectbox('Note :- Garage_Finish ', ['Unknown', 'Unf' , 'RFn' , 'Fin' ])


Garage_Cars = st.number_input('Note :- Garage_Cars' , min_value = 0.0 , max_value = None , step =0.1 )


Garage_Area = st.number_input('Note :- Garage_Area' , min_value = 0.0 , max_value = None , step =0.1 )



input_data = pd.DataFrame([{
    'Overall_Qual' : Overall_Qual, 
    'Year_Built' : Year_Built , 
    'Year_Remod_Add' : Year_Remod_Add , 
    'Mas_Vnr_Area' : Mas_Vnr_Area, 
    'Exter_Qual' : Exter_Qual, 
    'Bsmt_Qual' : Bsmt_Qual, 
    'BsmtFin_SF_1' : BsmtFin_SF_1, 
    'Total_Bsmt_SF' : Total_Bsmt_SF, 
    'Heating_QC' : Heating_QC , 
    'first_Flr_SF' : first_Flr_SF , 
    'Gr_Liv_Area' : Gr_Liv_Area, 
    'Full_Bath' : Full_Bath  , 
    'Kitchen_Qual' : Kitchen_Qual  , 
    'TotRms_AbvGrd' : TotRms_AbvGrd , 
    'Fireplaces' : Fireplaces , 
    'Fireplace_Qu' : Fireplace_Qu , 
    'Garage_Yr_Blt' : Garage_Yr_Blt , 
    'Garage_Finish' : Garage_Finish , 
    'Garage_Cars' :Garage_Cars, 
    'Garage_Area' : Garage_Area 
}])


if st.button("Predict House Price"):
    
    predict = model.predict(input_data)[0]
    
    prediction = np.round(predict , 3)
    
    st.success(f"🏠 Estimated House Price: $ {prediction}")
