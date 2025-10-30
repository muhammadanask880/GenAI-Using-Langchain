from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os                   
load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0, max_completion_tokens=500)
result = model.invoke("Write a poem about a lonely computer")
print(result)
#to print only content of the response
print(result.content)  