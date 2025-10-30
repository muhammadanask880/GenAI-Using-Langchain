from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
documents= ["I love programming in Python", "Python is a great programming language"]
vector = embeddings.embed_documents(documents)
print(vector)