from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text: str):
    spillter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = spillter.create_documents([text])
    return docs