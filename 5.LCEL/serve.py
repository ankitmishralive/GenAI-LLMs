


from fastapi import FastAPI
from langchain_groq import ChatGroq 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from pydantic import BaseModel
from langserve import add_routes  # For Creating API's
import os 
from dotenv import load_dotenv 
load_dotenv() 


# GROQ API KEY 
groq_api_key= os.getenv("GROQ_API_KEY")
# Model 
model=ChatGroq(model="Gemma-7b-It",groq_api_key=groq_api_key)



generic_template = "Translate the Following into {language} :"

parser = StrOutputParser() 

prompt = ChatPromptTemplate.from_messages(
[
    ("system",generic_template),
    ("user","{text}")
]
)


# Chain 
chain = prompt|model|parser 


# App Definition 
app = FastAPI(title="Langchain Server",
              version="v1",
              description="A simple API server  using Langchain runnable Interfaces"
              )

add_routes(
    app,
    chain,
    path ="/chain"
)




if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)









