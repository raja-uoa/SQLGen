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

from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
import google.generativeai
llm = GooglePalm(google_api_key=st.secrets['api_key'])

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
agent=create_pandas_dataframe_agent(llm,df)
agent.run("how many number of rows")
#return a sql with join between customer and customer_address based on fk with primary=true
