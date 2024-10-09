import os 
from dotenv import load_dotenv 
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate # design my own prompt template 
import streamlit as st 
from langchain_core.output_parsers import StrOutputParser # for outputting things properly 


load_dotenv() 

# langsmith tracking 
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
# langsmith tracing 
os.environ["LANGCHAIN_TRACING"] =  "true"
os.environ['LANGCHAIN_PROJECT_OPENSOURCE'] = os.getenv("LANGCHAIN_PROJECT_OPENSOURCE")





### Prompt Template 

prompt = ChatPromptTemplate.from_messages(

  [
      ('system',"Hey you are helpful assistant please respond to the question asked"),
      ('user','Question:{question}')
  ]

)


## Streamlit Framework 

st.title("Langchain Demo with LLama 3")

input_text = st.text_input("What questions you have in your mind ?")

## Ollama Model 2 

llm = Ollama(model='llama3.1')

output_parser = StrOutputParser() 

chain = prompt|llm|output_parser


if input_text:
    response=chain.invoke(
        {"question":input_text}
    )
    st.write(response)












