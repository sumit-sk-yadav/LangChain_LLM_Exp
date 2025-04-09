from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['LANGSMITH_TRACING'] = "true"
os.environ['LANGSMITH_API_KEY'] = os.getenv("LANGSMITH_API_KEY")

## prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an assistant. Please respond to the users questions"),
        ("user", "Question : {question}")
    ]
)

st.title("Basic Chatbot with DEEPSEEK")
input_text = st.text_input("Ask Away")


## Integrating the LLM
llm = Ollama(model = "deepseek-r1")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))