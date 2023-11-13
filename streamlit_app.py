import streamlit as st
import pandas as pd

# Streamlit app title
st.title("ST_Mapping TO Code")

# Text input widget
uploaded_file=st.file_uploader("Upload the STTM") 

if uploaded_file is not None:
#read excel
  df=pd.read_excel(uploaded_file)
  st.dataframe(df)
