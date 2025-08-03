# tests/test_embedder.py

from app.embedder import Embedder

def test_embed():
    embedder = Embedder()
    embeddings = embedder.embed(["hello", "world"])
    
    assert len(embeddings) == 2
    assert len(embeddings[0]) > 0
