import requests
import streamlit as st

def get_essay_response(input_text):
    response = requests.post("http://localhost:8000/essay",
                            json={'topic': input_text})
    print(response.json())
    return response.json()

def get_code_response(input_text):
    response = requests.post("http://localhost:8000/code",
                            json={'topic': input_text})
    print(response.json())
    return response.json()


st.title("langchain server deemo")
input_text1 = st.text_input("write an essay")
input_text2 = st.text_input("generate code for")

if input_text1:
    st.write(get_essay_response(input_text1))

if input_text2:
    st.write(get_code_response(input_text2))