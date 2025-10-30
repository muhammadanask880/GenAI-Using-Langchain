from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm1=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation")
model = ChatHuggingFace(llm=llm1)


chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to French."),
    ("human", "Translate the following English text to French: '{text}'")
])

prompt=chat_template.invoke({"text":"Hello, how are you?"})
print(prompt)
