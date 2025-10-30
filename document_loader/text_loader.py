from langchain_community.document_loaders import TextLoader

loader= TextLoader(r"C:\Users\anus.khan\Desktop\GEN AI MODELS\Document_Loader\cricket_poem.txt", encoding='utf-8')


docs=loader.load()
print(docs)

print("*******************************")

print(docs[0].page_content)

# to invoke in as prompt
# chain.invoke({'poem':docs[0].page_content})