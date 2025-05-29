from fastapi import FastAPI, UploadFile, File, Form
from app.utils.file_handler import load_file
from app.utils.text_chunker import chunk_text
from app.utils.embedder import embed_and_store, search_similar
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Dynamic File Embedding with Qdrant Vector DB API",
    description="API for uploading files, chunking text, embedding, and searching.",
    version="1.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    text = await load_file(file)
    chunks = chunk_text(text)
    embed_and_store(chunks)
    return {"message": f"Uploaded and embedded of {file.filename} successfully."}

@app.get("/search/")
async def search(query: str):
    results = search_similar(query)
    return JSONResponse(content=results)
