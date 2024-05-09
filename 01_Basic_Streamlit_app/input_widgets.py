import streamlit as st
import pandas as pd


# Button 

primary_btn=st.button(label="primary", type="primary")

if primary_btn:
    st.text("Primary btn pressed")

secondary_btn=st.button(label="secondary button", type="secondary")

if secondary_btn:
    st.text("secondary btn pressed")

st.divider()

# Checkbox

checkbox=st.checkbox("remember me ?")

if checkbox :
    st.text("remeber me ")
else:
    st.text("not remember me ")

st.divider()

# Select box

df=pd.read_csv("../NOTEBOOK/data/sample.csv")

select_Val=st.selectbox(label="choose a column", options=df.columns[1:],index=1)

st.write(f"selected value is :",{select_Val})
st.write(select_Val)

st.divider()


# Multi-select

select=st.multiselect(label="choose as many columns as you want :",options=df.columns[1:],max_selections=2)
st.write(select)

# Slider
st.divider()

slider = st.slider("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
st.write(slider)

# Text input
st.divider()

text_input = st.text_input("What's your name?", placeholder="John Doe")
st.write(f"Your name is {text_input}")

# Number input
st.divider()

num_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(f"You picked {num_input}")

# Text area
st.divider()

txt_area = st.text_area("What do you want to tell me?", height=500, placeholder="Write your message here")
st.write(txt_area)