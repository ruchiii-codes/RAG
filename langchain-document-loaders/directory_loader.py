from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',     # Path to the directory containing PDF files
    glob='*.pdf',     # gloab is a parameter that specifies the pattern to match files in the directory. In this case, it is set to '*.pdf', which means it will match all files with a .pdf extension in the specified directory.
    loader_cls=PyPDFLoader    # All files are pdf files, so we can directly use PyPDFLoader as the loader class to load the documents.
)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)