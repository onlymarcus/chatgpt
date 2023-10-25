import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import streamlit as st
st.title('My first app')
st.write('Hello world')
