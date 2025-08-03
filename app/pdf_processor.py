# app/pdf_processor.py

from pathlib import Path
import fitz  # PyMuPDF
from . import logger

class PDFProcessor:
    def extract_text(self, pdf_path: str) -> str:
        logger.info(f"Extracting text from {pdf_path}")
        text = ""
        try:
            doc = fitz.open(pdf_path)
            for page in doc:
                text += page.get_text()
            logger.info(f"Successfully extracted {len(text)} characters from {pdf_path}")
            return text
        except Exception as e:
            logger.exception(f"Failed to extract text from {pdf_path}: {e}")
            raise