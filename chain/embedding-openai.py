from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
text = "I love programming in Python"
vector = embeddings.embed_query(text)
print(vector)

