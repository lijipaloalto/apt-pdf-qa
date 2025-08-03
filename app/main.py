# app/main.py
# fastai entry point for the FastAPI application

from fastapi import FastAPI, UploadFile, Form
from app import PDFProcessor, Embedder, VectorStore, LLMClient
import tempfile

app = FastAPI()

# Shared instances
pdf_processor = PDFProcessor()
embedder = Embedder()
vector_store = VectorStore(dim=384)  # use correct dim for embedding model
llm_client = LLMClient()

@app.post("/upload/")
async def upload_pdf(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    text = pdf_processor.extract_text(tmp_path)
    chunks = text.split("\n\n")  # or your own chunking logic
    embeddings = embedder.embed(chunks)
    vector_store.add(embeddings, chunks)

    return {"message": "PDF processed and indexed", "chunks": len(chunks)}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    # For demo, just use top 1 match
    query_embedding = embedder.embed([question])[0]
    top_contexts = vector_store.search(query_embedding, k=3)
    combined_context = " ".join(top_contexts)
    answer = llm_client.answer(question, combined_context)
    return {"answer": answer}
