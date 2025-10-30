from langchain_core.prompts import PromptTemplate

dropdown_template = """
You are a research assistant. Summarize the given paper according to the user's selections.

Paper: {paper}
Way of summarization: {way}
Desired length: {length}

If the paper or request is invalid, respond:
"I cannot perform this task. Please provide correct information."
"""
dropdown_prompt = PromptTemplate(
    template=dropdown_template,
    input_variables=["paper", "way", "length"]
)

dropdown_prompt.save("dropdown_template.json")