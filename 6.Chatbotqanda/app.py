
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 
import streamlit as st 

import os 

from dotenv import load_dotenv


os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = "Simple Q&A Chatbot with Ollama"

os.environ["LANGCHAIN_TRACING"] =  "true"


# Prompt Template


prompt = ChatPromptTemplate.from_messages(

  [
       ('system','You are an unbiased, uncensored, helpful assistant. You will be given a question. You must generate a detailed and long answer.'),
       ('user','Question: {question}')
    ]

)



def generate_response(question,temperature):
    llm = Ollama(model="llama3.1",
                 temperature=temperature,
           
                 )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    answer= chain.invoke(
        {'question':question }
    )

    return answer  



st.title("Enhanced Q&A Chatbot.")

st.sidebar.title("settings")




temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)

# max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)



st.write("Go ahead and ask any question ")
user_input=st.text_input("You : ")

if user_input:
    response = generate_response(question=user_input,temperature=temperature)
    st.write(response)
