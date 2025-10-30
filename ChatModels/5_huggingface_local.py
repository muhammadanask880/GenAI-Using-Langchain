

from huggingface_hub import login
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Authenticate (use your Hugging Face token)

# Load the Llama model
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.1}
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("Write a poem about a lonely computer")
print(result.content)

