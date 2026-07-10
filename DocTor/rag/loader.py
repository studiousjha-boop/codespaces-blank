import fitz

def load_pdf(file_path):
    """
    Reads a PDF file and returns all extracted text as a single string.

    """

    text = ""

    doc = fitz.open(file_path)

    for page in doc:

        text += page.get_text()

    doc.close()

    return text