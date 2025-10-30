from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Load Hugging Face API token from .env
load_dotenv()

# Connect to Hugging Face Inference API
llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="text-generation"
)
model = ChatHuggingFace(llm=llm1)

# Define chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to French. "
               "Translate ONLY into French and never reply in English."),
    ("human", "Translate the following English text: '{text}'")
])

# Initialize chat history
chat_history = []

# Example input
user_input = "Hello, how are you?"

# Build prompt
prompt = chat_template.invoke({"text": user_input})
print("Messages:", prompt.to_messages())
print("-----")

# Convert to string so model respects instruction
prompt_str = prompt.to_string()
print("Formatted prompt string:\n", prompt_str)
print("-----")

# Get model response
result = model.invoke(prompt_str)
print("AI Response:", result.content)

# Save to history
chat_history.extend(prompt.to_messages())
chat_history.append(AIMessage(content=result.content))

# # Show full conversation history
# print("\n=== Chat History ===")
# for msg in chat_history:
#     role = msg.__class__.__name__.replace("Message", "")
#     print(f"{role}: {msg.content}")

print(chat_history)