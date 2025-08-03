# tests/test_pdf_processor.py

from app.pdf_processor import PDFProcessor
import os

def test_extract_text():
    processor = PDFProcessor()
    test_pdf = "tests/data/test_doc.pdf"
    
    # Create a dummy 1-page PDF
    if not os.path.exists(test_pdf):
        import fitz
        doc = fitz.open()
        page = doc.new_page()
        page.insert_text((72, 72), "Hello from test PDF.")
        doc.save(test_pdf)
        doc.close()
    
    text = processor.extract_text(test_pdf)
    assert "Hello from test PDF" in text
