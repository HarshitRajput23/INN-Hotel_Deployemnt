
import streamlit as st
import numpy as np
import pandas as pd

import pickle
with open('final_model_xgb.pkl','rb')as file:
    model = pickle.load(file)

with open('transformer.pkl','rb')as file:
    pt = pickle.load(file)

def prediction(input_list):

    input_list = np.array(input_list,dtype=object)
    
    pred = model.predict_proba([input_list])[:,1][0]
    
    if pred > 0.5:
        return f'This booking is more likely to get canceled : chances{round(pred,2)}'
    else:
        return f'This booking is less likely to get canceled : chances{round(pred,2)}'



def main():
    st.title('INN HOTEL GROUP')
    lt = st.text_input('Enter the lead time.')
    mst = (lambda x:1 if x=='Online' else 0)(st.selectbox('Enter the type of booking',['Online','Offline']))
    spcl = st.selectbox('Selct the no of special request made',[0,1,2,3,4,5,])
    price = st.text_input('Enter the price of offered for the room')
    adults = st.selectbox('Select the no of Adults in bookning',[0,1,2,3,4])
    wkd = st.text_input('Enter the weekend nights in booking')
    wk = st.text_input('Enter the week nights in booking')
    park = (lambda x:1 if x=='Yes' else 0)(st.selectbox('Is parking included in the booking',['Yes','No']))
    months = st.slider('What will be month of arival',min_value=1,max_value=12,step=1)
    day = st.slider('What will be day of arival',min_value1,max_value=31,step=1)
    wkday_lambda = (lambda x:0 if x=='Mon' else 1 if x=='Tues' else 2 if x=='Wed' else 3 if x=='Thur' else 4 if x=='Fri' else 5 if x=='Sat' else 6 )
    wkday = st.selectbox('What is the weekday of arrival',['Mon','Tues','Wed','Thur','Fri','Sat','Sun'])
    
    trans_data = pt.transform ([[lt,price]])
    lt_t = tran_data[0][0]
    price_t = tran_data[0][1]
    
    inp_list = [lt_t,mst,spcl,price_t,adults,wkd,park,wk,month,day,wkday]
    
    if st.button('Predict'):
        response = prediction(inp_list)
        st.success(response)

if __name__=='__main__':
    main()
