import streamlit as st
import pandas as pd
import joblib

model = joblib.load('uci_retail_cluster.pkl')


st.title('UNSUPERVISED MACHINE LEARNING PROBLEM')
st.divider()

st.header('UCI ONLINE RETAIL PREDICTION SUSTSEM')

st.divider()

st.subheader('PROBLEM STATEMENT :- MAKING A SOLUTION FOR A CUSTOMER OF A UCI ONLINE RETAIL ON THE BASIC OF A FEATURES AND FORMING A CLUSTER ')

st.divider()


st.subheader('Quantity')
Quantity = st.number_input('Note : -Quantity ' , min_value = 0 , max_value = None , step = 1)


st.subheader('Country')
Country = st.selectbox('Note :- Country' , ["United_Kingdom", "Germany", "France", "EIRE", "Spain", "Netherlands", "Belgium", "Switzerland", "Portugal", "Norway", "Australia", "Italy", "Sweden", "Unspecified", "Finland", "Channel_Islands", "Cyprus", "Denmark", "USA", "Iceland", "Austria", "Hong_Kong", "Japan", "Singapore", "Bahrain", "RSA", "Canada", "Poland", "Israel", "United_Arab_Emirates", "Greece", "Lithuania", "European_Community"] )


st.subheader('UnitPrice')
UnitPrice = st.number_input('Note : - UnitPrice' , min_value = 0.0 , max_value = None , step = 1.0)

st.subheader('day')
day = st.number_input('Note :day ' , min_value = 1, max_value = 31 , step = 1)


st.subheader('month')
month = st.number_input('Note : - month ' , min_value = 1, max_value = 12 , step = 1)


st.subheader('year')
year = st.selectbox('Note :- year' , [2010 , 2011])


input_data = pd.DataFrame([{
    'Quantity' : Quantity, 
    'UnitPrice' : UnitPrice , 
    'Country' : Country , 
    'day' : day , 
    'month'  : month , 
    'year' : year 
}])


if st.button('Predict'):
    
    predict = model.predict(input_data)[0]
    
    prediction = {0 : 'Daily'  , 1 : 'Weekend' , 2 : 'Ocassionaly'}.get(predict)
    
    st.success(f'As per the Data The Customer is **{prediction}**')
    
    