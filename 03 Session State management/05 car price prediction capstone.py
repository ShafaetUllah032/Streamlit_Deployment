import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

if "pred" not in st.session_state:
    st.session_state["pred"]=None



dc=dict()
def creating_required_data(mf):
    f_columns=mf.columns
    for c in f_columns:
        #print(mf[c].unique())
        l=mf[c].unique()
        dc[c]=l


@st.cache_resource(show_spinner="loading model ..... ")
def model_loader():
    model=load("../NOTEBOOK/model/car_model.joblib")
    return model

def make_prediction(pipe):
    miles=st.session_state['miles']
    year=st.session_state['year']
    make=st.session_state['make']
    e_size=st.session_state['engine_size']
    model=st.session_state['model']
    state=st.session_state['location']
    X_pred=np.array([miles,year,make,model,e_size,state])
    X_pred=[X_pred]
    pred=pipe.predict(X_pred)
    pred=round(pred[0],2)
    st.session_state['pred']=pred


if __name__=="__main__":

    st.title("🚲 Car Price calculator")

    mf=pd.read_csv("../NOTEBOOK/data/honda_toyota_ca.csv")
    mn=float(min(mf['miles']))
    mx=float(max(mf['miles']))
    df= mf[['year','make','model','state']]

    creating_required_data(mf=df)

    pipe=model_loader()

    with st.form("value collection "):

        col1,col2=st.columns(2)

        with col1:
            st.number_input("miles",min_value=mn,max_value=mx,step=500.0,key='miles')
            st.selectbox("year",options=list(dc['year']),key="year")
            st.selectbox('Brand',options=list(dc['make']),key="make")
        
        with col2:
            st.number_input("engine size",min_value=0.5,max_value=6.0,step=.1,key="engine_size")
            st.selectbox("model",options=list(dc['model']),key="model")
            st.selectbox("Province",options=list(dc['state']),key="location")

        st.form_submit_button("calculate",type="primary",on_click=make_prediction,kwargs=dict(pipe=pipe))


    if st.session_state["pred"] is not None:
        st.subheader(f"The estimated car price is : {st.session_state.pred} $")
    else:
        st.write("Input information and click on Calculate to get an estimated price")
    
    st.write(st.session_state)    