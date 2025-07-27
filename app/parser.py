import fitz  # PyMuPDF

def extract_sections(pdf_path, document_name):
    doc = fitz.open(pdf_path)
    sections = []
    for i, page in enumerate(doc):
        text = page.get_text()
        if len(text.strip()) < 50:
            continue
        sections.append({
            "document": document_name,
            "page": i + 1,
            "text": text.strip()
        })
    return sections
