import os
import streamlit as st 
from langchain.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] =os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] =os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'True'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')


st.title("This is a Simple App using OLLAMA")
input = st.text_input("Please type your question.")


prompt = ChatPromptTemplate.from_messages(
[
    ("system", "You are an AI assistant.Respond to the questions they asked"),
    ("user", "Given the context: {question}")
]
)

llm =Ollama(model="gemma2:2b")
output_parse = StrOutputParser()
chain = prompt|llm|output_parse

if input:
    st.write(chain.invoke({"question": input}))

