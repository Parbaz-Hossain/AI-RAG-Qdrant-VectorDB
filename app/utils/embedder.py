from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient

# Load Embedding model once
embedding_model = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-base-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False}
)

# Connect to Qdrant and store the embeddings
url="http://localhost:6333"
collection_name = "dynamic_files_db"

def embed_and_store(docs):
    Qdrant.from_documents(
        documents=docs,
        embedding=embedding_model,
        url=url,
        prefer_grpc=False,
        collection_name=collection_name
    )

# Symentic search function
qdrant_client = QdrantClient(
    url = url,
    prefer_grpc = False
)

def search_similar(query, k=2):
    vector_store = Qdrant(
        client=qdrant_client,
        embeddings=embedding_model,
        collection_name=collection_name
    )
    results = vector_store.similarity_search_with_score(query, k=k)
    return [{"Score": score, "Content": doc.page_content, "Metadata": doc.metadata} for doc, score in results]



