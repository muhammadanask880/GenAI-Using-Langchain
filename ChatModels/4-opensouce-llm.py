#open source llm models are free to use that can ve downloaded and run locally on your machine
#they can be modified , fine tuned as per your requirements
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm1=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation",
                         max_new_tokens=10)
model =ChatHuggingFace(llm=llm1)

result=model.invoke("What is capital of india?")
# print(result)
print(result.content)

