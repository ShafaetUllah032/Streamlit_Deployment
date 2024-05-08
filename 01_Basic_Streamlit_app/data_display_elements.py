import streamlit as st
import pandas as pd
import numpy as np


df=pd.read_csv("../NOTEBOOK/data/sample.csv",index_col=False)


st.write(df)

st.divider()

st.dataframe(df)

st.divider()


st.table(df)

st.divider()


st.metric(label="Expenses",value=900, delta=-20, delta_color="inverse")
