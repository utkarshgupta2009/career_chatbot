# config.py
from dotenv import load_dotenv
import os
import google.generativeai as genai
import emoji
import streamlit as st

load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit configuration
def setup_streamlit():
    st.set_page_config(
        layout="wide", 
        page_title="Career Advisor",
        page_icon=emoji.emojize(':robot:'), 
        menu_items=None
    )
    
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.title(f"Career Advisor Chatbot {emoji.emojize(':robot:')}")
