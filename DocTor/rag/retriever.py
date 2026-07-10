from rag.embeddings import create_embeddings
from rag.vector_store import search_index
from settings import TOP_K

def retrieve(question, index, chunks):
    # Step 1: Create embedding for the user's question
    question_embedding = create_embeddings([question])

    _, indices =search_index(
        index, 
        question_embedding,
        TOP_K
    ) 

    print("Indices:", indices)
    print("Retrieved Chunks:")

    for i in indices[0]:
        print(f"\nChunk {i}:")
        print(chunks[i][:200])

    return [chunks[i] for i in indices[0]]