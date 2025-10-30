from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv  
import os                 
load_dotenv()   
model = ChatGoogleGenAI(model="gemini-1.5-pro")
result = model.invoke("Write a poem about a lonely computer")           
print(result)
#to print only content of the response  
print(result.content)   
