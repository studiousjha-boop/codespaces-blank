from rag.embeddings import create_embeddings
from settings import TOP_K

def retrieve(question, index, chunks):
    # Step 1: Create embedding for the user's question
    question_embedding = create_embeddings([question])

    # Step 2: Search the vector database
    distances, indices = index.search(question_embedding, TOP_K)

    # Step 3: Convert indices back to text chunks
    retrieved_chunks = [chunks[i] for i in indices[0]] 

    return retrieved_chunks