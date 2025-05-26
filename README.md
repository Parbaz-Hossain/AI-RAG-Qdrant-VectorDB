# AI-RAG-Qdrant-VectorDB

A minimal and efficient Retrieval-Augmented Generation (RAG) pipeline using **Python** and **Qdrant** Vector Database.

## 🚀 Features

- 🔎 Embedding & indexing of documents (PDF) into Qdrant
- 🧠 Retrieval-Augmented QA with GPT-based models
- 📂 Organized structure for ingestion, retrieval, and querying
- ⚙️ Easy to extend for multi-source data and LLM integration

## 📁 Project Structure

- `app.py` – Main FastAPI app for querying
- `ingest.py` – Script to load and embed documents into Qdrant
- `collections/gpt_db` – Qdrant DB files (local instance)
- `requirements.txt` – Python dependencies
- `data.pdf` – Sample document used for testing

## ✅ Getting Started

```bash
# Clone repo
git clone https://github.com/parbaz-hossain/AI-RAG-Qdrant-VectorDB.git
cd AI-RAG-Qdrant-VectorDB

# Create virtual environment & install dependencies
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run ingestion script
python ingest.py

# Start API server
python app.py
