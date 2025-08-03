# 📄 PDF Q&A Tool

A lightweight, local-first PDF Question Answering app powered by **FastAPI**, **Streamlit**, **FAISS**, and **LLMs** like **LLaMA3** via Ollama. It lets you upload PDFs, ask questions, and get answers grounded in the document content.

---

## 🔧 Features

- 📚 PDF text extraction via `PyMuPDF`
- 💡 Question Answering using LLaMA3 (via Ollama API)
- 🧠 Embedding with `multi-qa-mpnet-base-dot-v1`
- 🔎 Similarity search with `FAISS`
- 🚀 Web API via FastAPI
- 🖼️ Streamlit UI for quick interaction
- 💾 Local embedding cache
- 📜 Logging of all major components
- ✅ Unit tests with pytest

---

## 📁 Project Structure

```
pdf-qa-app/
│
├── app/
│   ├── __init__.py
│   ├── pdf_processor.py      # Extract text from PDFs
│   ├── vector_store.py       # Embedding + FAISS storage + caching
│   ├── llm_client.py         # LLaMA3 API wrapper via Ollama
│   ├── config.py             # Configuration variables
│   └── api.py                # FastAPI endpoints (optional)
│
├── streamlit_app.py         # Streamlit UI entrypoint
├── tests/
│   ├── test_pdf_processor.py
│   ├── test_vector_store.py
│   ├── test_llm_client.py
│
├── logs/                    # Logs saved locally
├── vector_cache/           # Saved FAISS indexes and texts
├── requirements.txt
├── README.md
└── main.py                  # Entrypoint (FastAPI or CLI)
```

---

## 🚀 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourname/pdf-qa-app.git
cd pdf-qa-app
```

### 2. Create and activate virtualenv
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Ollama (if not already)
```bash
ollama serve
ollama run llama3
```

### 5. Run the app
#### FastAPI
```bash
uvicorn main:app --reload --port 8000
```
#### Streamlit UI
```bash
streamlit run streamlit_app.py
```

---

## Run Tests

```bash
pytest tests/
```

## / Run the App
```bash
streamlit run streamlit_app/streamlit_app.py
```
---

## ⚙️ Configuration

Modify `app/config.py`:

```python
EMBEDDING_MODEL = "multi-qa-mpnet-base-dot-v1"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
VECTOR_CACHE_DIR = "vector_cache"
```

---

## 📈 Logs

Logs are saved to the `logs/` directory per component:
- `pdf_processor.log`
- `vector_store.log`
- `llm_client.log`

---

## ✅ TODOs

- [x] Add Streamlit UI
- [ ] Enhance logging module
- [ ] Upload multiple PDFs
- [ ] Support multiple LLMs via config
- [ ] Dockerize the app
- [ ] Add authentication (optional)
- [ ] Switch from transformers pipeline to vLLM, Ollama, or LangChain for RAG enhancements

---

## 📜 License

MIT License © 2025 Li Ji
