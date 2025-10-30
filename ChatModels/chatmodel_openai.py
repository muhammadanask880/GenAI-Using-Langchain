from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

#temprature controls randomness. 0 means more deterministic output
#max_completion_tokens controls the length of the output

llm = ChatOpenAI(model="gpt-4", temperature=0, max_completion_tokens=500)
result = llm.invoke("Write a poem about a lonely computer")
print(result)

#to print only content of the response
print(result.content)
