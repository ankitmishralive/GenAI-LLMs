
import streamlit as st 

import os 
import pydantic.v1
from dotenv import load_dotenv 
from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv() 
groq_api_key= os.getenv("GROQ_API_KEY")





# model

# prompt 

prompt = ChatPromptTemplate.from_messages(
    [
       ('system','You are helpful assistant. Please response to the user queries'),
       ('user','Question: {question}')
    ]
)

def generate_response(question,llm,temperature,max_tokens,groq_api_key):
    question 
    llm=ChatGroq(model=llm,
                 groq_api_key=groq_api_key,
                 temperature=temperature,
                 max_tokens=max_tokens,      
                 )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    answer= chain.invoke(
        {'question':question }
    )

    return answer  


st.title("Enhanced Q&A Chatbot.")

st.sidebar.title("settings")

api_key = st.sidebar.text_input("Enter your Groq Api key: ",type="password")

## Dropdown 



llm = st.sidebar.selectbox("Select a Model", [
    "distil-whisper-large-v3-en",
    "gemma2-9b-it",
    "gemma-7b-it",
    "llama3-groq-70b-8192-tool-use-preview",
    "llama3-groq-8b-8192-tool-use-preview",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "llama-guard-3-8b",
    "llava-v1.5-7b-4096-preview",
    "llama3-70b-8192",
    "llama3-8b-8192",
    "mixtral-8x7b-32768",
    "whisper-large-v3"
])


temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)

max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)



st.write("Go ahead and ask any question ")
user_input=st.text_input("You : ")

if user_input:
    response = generate_response(question=user_input,llm=llm,groq_api_key=api_key,temperature=temperature,max_tokens=max_tokens)
    st.write(response)
