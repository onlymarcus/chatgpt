import os
import openai
import streamlit as st

openai.api_key = st.secrets["api_secret"]
# Para o streamlit é melhor usar esse tipo de chave da  openai.
#cria um arquivo com extensão .toml e salva na pasta .streamlit

# Create Text Area Widget to enable user to enter texts
article_text = st.text_area("enter text")

# Create Radio Buttons

