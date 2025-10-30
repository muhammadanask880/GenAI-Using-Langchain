from langchain_community.document_loaders import PyPDFLoader
# as much pages as much documents will be created in pypdf so remember that thing as well.

# it is not good for all pdfs like scanned file, complex layouts and etc so use another one

# see langchain dcumentaion for different loaders
loader= PyPDFLoader(r"C:\Users\anus.khan\Desktop\GEN AI MODELS\Document_Loader\basic-text.pdf")


docs=loader.load()
print(docs)

print("*******************************")

print(docs[0].page_content)

# to invoke in as prompt
# chain.invoke({'poem':docs[0].page_content})

