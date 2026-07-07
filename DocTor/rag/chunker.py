def chunk_text(text, chunk_size = 500, overlap = 100):
    """
    Splits text into overlapping chunks.

    """

    chunks = []

    step = chunk_size - overlap

    for i in range (0, len(text), step):
        chunk = text[i:i +chunk_size]

        if chunk:
            chunks.append(chunk)

    
    return chunks