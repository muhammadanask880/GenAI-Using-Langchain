from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

#note 
#that directly use .load() will load everything in memory which is not possible if you have very long files and too much files
#.lazy_load use to load one doucment at runtimr and work well if you have so many documents



# loader = DirectoryLoader(
#     path= r"Document_Loader/pdf_files",
#     glob="*.pdf",
#     loader_cls=PyPDFLoader
# )

# docs=loader.load()

# print(docs)

# print("**************************")

# print()

# print(len(docs))



loader1 = DirectoryLoader(
    path= r"Document_Loader/pdf_files",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs1=loader1.lazy_load()
for i in docs1:
    print(i)