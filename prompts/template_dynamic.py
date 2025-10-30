#advantages of using propmt template with dynamic input
#user can select from dropdown or enter own query
#based on user selection different prompt template will be used   

#advantages of prompt template over f-string 
#1. Reusability:  template can saved Prompt templates allow you to define a prompt structure once and reuse it multiple times with different inputs. This is especially useful when you have a consistent format for your prompts but need to change specific details.
#2. validation: Prompt templates can help ensure that the input variables are correctly formatted and validated before being used in the prompt. This can reduce errors and improve the quality of the generated text.


import streamlit as st
from langchain_core.prompts import PromptTemplate ,load_prompt
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv      

load_dotenv()

# Load model
model = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="text-generation"
)
llm = ChatHuggingFace(llm=model)

st.title("📚 Research Assistant")

# --- Templates ---
# dropdown_template = """
# You are a research assistant. Summarize the given paper according to the user's selections.

# Paper: {paper}
# Way of summarization: {way}
# Desired length: {length}

# If the paper or request is invalid, respond:
# "I cannot perform this task. Please provide correct information."
# """

own_query_template = """
You are a research assistant. Answer the following user query directly.
If the query is unclear or invalid, respond:
"I cannot perform this task. Please provide correct information."

Query: {query}
"""

# dropdown_prompt = PromptTemplate(
#     template=dropdown_template,
#     input_variables=["paper", "way", "length"]
# )
dropdown_prompt = load_prompt(r"C:\Users\anus.khan\Desktop\GEN AI MODELS\dropdown_template.json")



own_query_prompt = PromptTemplate(
    template=own_query_template,
    input_variables=["query"]
)

# --- Mode selection ---
mode = st.radio(
    "Choose input method:",
    ["Use Dropdowns", "Enter Own Prompt"]
)

if mode == "Use Dropdowns":
    # Dropdowns
    paper = st.selectbox("Select Paper", [
        "Attention is All You Need", 
        "Word2Vec", 
        "Generative Adversarial Networks (Goodfellow et al., 2014)"
    ])
    way = st.selectbox("Select Way", ["Summary", "Key Points", "Abstract"])
    length = st.selectbox("Select Length", ["Short", "Medium", "Long"])

    if st.button("Generate Response"):
        final_prompt = dropdown_prompt.format(
            paper=paper,
            way=way,
            length=length
        )
        result = llm.invoke(final_prompt)
        st.write(result.content)

elif mode == "Enter Own Prompt":
    query = st.text_area("Enter your query:")

    if st.button("Generate Response"):
        final_prompt = own_query_prompt.format(query=query.strip())
        result = llm.invoke(final_prompt)
        st.write(result.content)
