from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## fUNTION TO LOAD GEMINI PRO MODEL AND GET RESPONSE

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

## INITIALIZE OUR STREAMLIT APP

st.set_page_config(page_title = "Gemini Image Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input Prompt: ", key = "input")

Uploaded_file = st.file_uploader("Choose an Image ... ",type = ["jpg","jpeg","png"])
image = ""

if Uploaded_file is not None:
    image = Image.open(Uploaded_file)
    st.image(image,caption = "Uploaded Image.", use_column_width = True)


submit = st.button("Tell me about this image")

# IF SUBMIT IS CLICKED

if submit:  
    response = get_gemini_response(input, image)
    st.subheader("The Response Is : ")
    st.write(response)
