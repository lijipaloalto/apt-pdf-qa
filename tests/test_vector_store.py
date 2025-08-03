# tests/test_vector_store.py

from app.vector_store import VectorStore
import numpy as np

def test_vector_add_and_search():
    store = VectorStore(dim=3)
    vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    texts = ["x", "y", "z"]

    store.add(vectors, texts)
    result = store.search([1, 0, 0], k=1)

    assert result == ["x"]
