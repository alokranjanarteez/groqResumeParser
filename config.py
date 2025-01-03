import os
import streamlit as st

os.environ['GROQ_API_KEY'] =  st.secrets['GROQ_KEY'] 

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0
MAX_RETRIES = 2