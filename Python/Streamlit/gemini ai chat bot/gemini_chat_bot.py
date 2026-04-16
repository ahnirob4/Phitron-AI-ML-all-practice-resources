from google import genai
import os 
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

api_key = os.environ.get('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

st.title(":red[**AI chat bot**]", anchor=False)
st.divider()

text = st.text_input('Prompt here', placeholder='Ask the AI')


if st.button('Execute Prompt'):
    if text:
        st.subheader('AI response: ', anchor=False)
        response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents= text)
        st.markdown(response.text)
    else:
        st.warning('Please give me a prompt first.')