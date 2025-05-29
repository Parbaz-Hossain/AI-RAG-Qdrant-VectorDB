from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter  


loader = PyPDFLoader("data3.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

texts = text_splitter.split_documents(documents)

# Load the embeddings model
model_name = "BAAI/bge-base-en-v1.5"
model_kwargs = {'device':'cpu'}
encode_kwargs = {'normalize_embeddings': False}

embeddings = HuggingFaceBgeEmbeddings(
    model_name = model_name,
    model_kwargs = model_kwargs,
    encode_kwargs = encode_kwargs
)
print("Embedding model loaded............")

# Create the Qdrant vector store
url = 'http://localhost:6333'
collection_name = 'gpt_db'

qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    url=url,
    prefer_grpc = False,
    collection_name=collection_name
)
print("Qdrant Index Created...............")