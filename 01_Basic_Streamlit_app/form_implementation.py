import streamlit as st
import pandas as pd

with st.form("form_key"):
    st.write("I am here to listen everything about you ")
    appetizer=st.selectbox(label="Appetizer",options=["choice 1","choice 2", "choice 3"])
    main=st.selectbox(label="Main Course",options=["choice 1","choice 2", "choice 3"])
    dessert=st.selectbox(label="Dessert",options=["choice 1","choice 2", "choice 3"])

    wine= st.checkbox("Are you bringing wine ?")

    visit_data=st.date_input("When are you coming ?")

    visit_time=st.time_input("when are you coming ? ")

    allergies=st.text_area("Any allergies ?",placeholder="Leave us a note for allergies")
    submit_btn=st.form_submit_button("submit")


st.write(f""" Your Oder summery:
         
Appetiser  : {appetizer}

Main Course: {main}

Dessert    : {dessert}

Are you bringing your own wine: {"yes" if wine else "no" }

Date of visit:{visit_data}

Time of visit : {visit_time}

Allergies     : {allergies}
         
""")

    