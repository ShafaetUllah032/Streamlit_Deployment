import streamlit as st

from datetime import datetime,timedelta


st.title("Advanced state Management")
 
# Store widget value in session state
st.subheader("Store widget value in session state")

st.slider("select a number ", 0,10)

st.write(st.session_state)

# Initialize widget value with session state 

st.subheader("Initialize widget value with session state")

if "num_input" not in st.session_state:
    st.session_state["num_input"]=5

st.number_input("pick a number ",0,10,key="num_input")

# Callbacks
  
st.subheader("Use callbacks")

st.markdown(" ### Select your time range")

def add_time_delta():
    intial=st.session_state['start_date']
    
    if st.session_state['radio_state']=='7 days':
        st.session_state['end_date']=intial + timedelta(days=7)
    
    elif st.session_state["radio_state"]=="28 days":
        st.session_state['end_date']=intial+timedelta(days=28)
    
    else:
        pass

def sub_time_delta():
    final=st.session_state['end_date']
    
    if st.session_state['radio_state']=='7 days':
        st.session_state['start_date']=final - timedelta(days=7)
    
    elif st.session_state["radio_state"]=="28 days":
        st.session_state['start_date']=final - timedelta(days=28)
    
    else:
        pass

st.radio("select a range" , ["7 days", "28 days","custom"], horizontal=True,key="radio_state",on_change=add_time_delta)
  
col1,col2=st.columns(2)

with col1:
    st.date_input("start date",key="start_date",on_change=add_time_delta)

with col2:
    st.date_input("end date",key="end_date",on_change=sub_time_delta)