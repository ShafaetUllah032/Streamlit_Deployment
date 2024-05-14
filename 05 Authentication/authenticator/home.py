import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


# Hash password and store then in the YAML file. Only do this once





st.title("Let's Learn the authentication process")

st.write(st.session_state)