import streamlit as st
import pandas as pd

# give you a app title
st.title("Text Element Streamlit")

# Header
st.header("Basic app fundamentals")

# Sub header 
st.subheader("working to handle text")

# markdown
st.markdown('''
...     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
...     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

# Caption
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# Code block

st.code( """ import numpy as np \n np.asarray(img) \n plt.imshow(img)""" )

# preformated text

st.text("Raw text")

# Latex
st.latex("2^2 = 4")

# Divider

st.text("upper part")
st.divider()
st.text("lower part")

# st.wrtie

st.write("Some raws text , with write options")

st.divider()

