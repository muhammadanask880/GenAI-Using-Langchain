from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os   
load_dotenv()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text = "I love programming in Python"
vector = embeddings.embed_query(text)
print(vector)   

# to embed documents
# documents= ["I love programming in Python", "Python is a great programming language"]     
# vector = embeddings.embed_documents(documents)
# print(vector) 
