# app/vector_store.py

import faiss
import numpy as np
from . import logger

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        logger.info(f"Initialized FAISS index with dimension: {dim}")

    def add(self, vectors, texts):
        self.index.add(np.array(vectors).astype('float32'))
        self.texts.extend(texts)
        logger.info(f"Added {len(texts)} items to FAISS store")

    def search(self, query_vector, k=3):
        D, I = self.index.search(np.array([query_vector]).astype('float32'), k)
        return [self.texts[i] for i in I[0] if i < len(self.texts)]


