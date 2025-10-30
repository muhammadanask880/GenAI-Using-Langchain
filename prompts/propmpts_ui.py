# this is static propmt not dynamic 
#that user can enter anything any on prompt LLM respons depend to much 
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
llm1= HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation")
model = ChatHuggingFace(llm=llm1)
#create a streamlit app to take input from user and display the output
st.title("Research Assistant")      
prompt = st.text_input("Enter your prompt")
if prompt:
    result=model.invoke(prompt)
    st.write(result.content)

