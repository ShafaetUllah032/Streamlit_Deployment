import streamlit as st
from joblib import load
import pandas as pd

dc=dict()

def creating_required_data(mf):
    f_columns=mf.columns
    for c in f_columns:
        #print(mf[c].unique())
        l=mf[c].unique()
        dc[c]=l
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    pipe=load("../NOTEBOOK/model/mushrooms_model.joblib")
    return pipe

def make_prediction(_pipe,x_pred):
    x_pred=[x_pred]
    pred = _pipe.predict(x_pred)
    return pred[0]


if __name__=="__main__":

    st.title("Mashrooms classifier 🍄")
    mf=pd.read_csv("../NOTEBOOK/data/mushrooms_final.csv")
    cols=mf.columns

    with st.expander("SEE THE SAMPLE DATA"):
        st.write(mf)

    st.subheader("Step 1 : Select the values for predictions..")

    creating_required_data(mf)

    col1,col2,col3=st.columns(3)

    with col1:
        a,b,c=cols[:3]
        a_list=list(dc[a])
        b_list=list(dc[b])
        c_list=list(dc[c])
        odor=st.selectbox(label=a,options=a_list)
        gill_size=st.selectbox(label=b,options=b_list)
        gill_color=st.selectbox(label=b,options=c_list)
    
    with col2:
        a,b,c=cols[3:6]
        a_list=list(dc[a])
        b_list=list(dc[b])
        c_list=list(dc[c])
        stalk_surface_above_ring=st.selectbox(label=a,options=a_list)
        stalk_surface_below_ring=st.selectbox(label=b,options=b_list)
        stalk_color_above_ring=st.selectbox(label=b,options=c_list)

    with col3:
        a,b,c=cols[6:9]
        a_list=list(dc[a])
        b_list=list(dc[b])
        c_list=list(dc[c])
        stalk_color_below_ring=st.selectbox(label=a,options=a_list)
        ring_type=st.selectbox(label=b,options=b_list)
        spore_print_color=st.selectbox(label=b,options=c_list)

    
    st.subheader("Step 2: Predict the condition of the mushroom..")

    pred_btn=st.button("Predict",type="primary")

    if pred_btn:
        pipe=load_model()

        x_pred = [odor, 
                  gill_size, 
                  gill_color, 
                  stalk_surface_above_ring, 
                  stalk_surface_below_ring, 
                  stalk_color_above_ring, 
                  stalk_color_below_ring, 
                  ring_type, 
                  spore_print_color]
        
        pred=make_prediction(pipe,x_pred)
        if pred=="p":
            st.write("The mushroom has poision☠️")
        else:
            st.write("The mushroom is absolutely eatable 🥗 . .")
