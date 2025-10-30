from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="filepath")
docs = loader.load()

print(docs)

#every row in csv will be consider as single unique doc
