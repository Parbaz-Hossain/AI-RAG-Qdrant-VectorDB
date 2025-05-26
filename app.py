from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient


# Load the embeddings model
model_name = "BAAI/bge-base-en-v1.5"
model_kwargs = {'device':'cpu'}
encode_kwargs = {'normalize_embeddings': False}

embeddings = HuggingFaceBgeEmbeddings(
    model_name = model_name,
    model_kwargs = model_kwargs,
    encode_kwargs = encode_kwargs
)

# Create the Qdrant vector store
url = 'http://localhost:6333'
collection_name = 'gpt_db'

client = QdrantClient(
    url = url,
    prefer_grpc = False
)

print("############# CLIENT ###############")
print(client)

db = Qdrant(
    client = client,
    embeddings = embeddings,
    collection_name = collection_name
)

print("############## DB ###############")
print(db)

query = "What is the bill address?"
docs = db.similarity_search_with_score(query, k = 1)
for i in docs:
    doc, score = i
    print("-------------------- START OF RESULT ------------------------------")
    print("Score:", score, "Content:", doc.page_content, "Metadata:", doc.metadata)
    print("-------------------- END OF RESULT   ------------------------------")