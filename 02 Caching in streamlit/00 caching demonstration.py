import streamlit as st
import time 
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


st.title("Cachine demonstration")

st.button("Test Cache")

st.subheader("st.cache_data")

@st.cache_data
def cache_this_function():
    time.sleep(5)
    out="I am done running "
    return out

out=cache_this_function()
st.write(out)

st.subheader("st.cache_resource")

@st.cache_resource
def create_simple_linear_regression():
    time.sleep(2)
    x=np.arange(0,100,2).reshape(-1,1)
    y=x*3+2
    
    model=LinearRegression().fit(x,y)

    return model

lr=create_simple_linear_regression()

x_pred=np.arange(1,13,2).reshape(-1,1)
pred=lr.predict(x_pred)

x_pred=x_pred.reshape(6)
pred=pred.reshape(6)

st.write(f"""
input value: {x_pred} 

output value: {pred}
""") 


