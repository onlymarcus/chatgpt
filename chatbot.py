import os
import openai
import streamlit as st
import numpy as np

openai.api_key = st.secrets["api_secret"]
# Para o streamlit é melhor usar esse tipo de chave da  openai.
# cria um arquivo com extensão .toml e salva na pasta .streamlit

with st.chat_message("user"):
    st.write("Hello")
    st.bar_chart(np.random.randn(30, 3))

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt:  {prompt}")
