from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()   


class Review(BaseModel):
    review: Literal['pos','neg'] = Field(description="give the sentiment of review in single word as pos or neg")

parser= StrOutputParser()
parser2= PydanticOutputParser(pydantic_object=Review)


llm1= HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation",
                         max_new_tokens=10)     
model = ChatHuggingFace(llm=llm1)


#classift the sentiment of review
template1 = """Classify the sentiment of this review in single word as Positive, Negative: {review}. and here is format instructions: {format_instructions}"""
prompt1 = PromptTemplate(template=template1, input_variables=["review"], partial_variables={"format_instructions": parser2.get_format_instructions()})

classify_chain = prompt1 | model | parser2
# result= classify_chain.invoke({"review": "The movie was fantastic! I really enjoyed it."}).review
# # print(result)

prompt2 = PromptTemplate(
    template ="write an appropriate single response to this review if the sentiment is positive: \n {review}",
    input_variables=["review"]
)

prompt3 = PromptTemplate(
    template ="write an appropriate single response to this review if the sentiment is negative: \n {review}",
    input_variables=["review"]
)

branch_chain = RunnableBranch(
    (lambda x: x.review == "pos",prompt2 | model | parser),
    (lambda x: x.review == "neg", prompt3 | model | parser),
    RunnableLambda(lambda x: "not find any senetiment")
)

final_chain = classify_chain | branch_chain
result= final_chain.invoke({"review": "The movie was bad terrible."})
print(result)
