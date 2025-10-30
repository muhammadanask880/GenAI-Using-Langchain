from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import os   
load_dotenv()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  

# to embed documents
documents= ["I love programming in Python", "i play cricket on weekends", "she loves to dance", "Python is a great programming language"]     
vector = embeddings.embed_documents(documents)
query= "I enjoy coding in Python"
query_vector= embeddings.embed_query(query)
similarity_scores= cosine_similarity([query_vector], vector)
#print top 3 similar documents
top_indices= similarity_scores[0].argsort()[-3:][::-1]
for index in top_indices:
    print(f"Document: {documents[index]}, Similarity Score: {similarity_scores[0][index]}")
