# app/__init__.py

import logging

# Configure global logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# Optional: create a logger object to import elsewhere
logger = logging.getLogger("pdf-qa-app")

# Expose components
from .pdf_processor import PDFProcessor
from .embedder import Embedder
from .vector_store import VectorStore
from .llm_client import LLMClient
