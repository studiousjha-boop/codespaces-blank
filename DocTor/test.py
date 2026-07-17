from rag.embeddings import create_embeddings

text = [
    "Artificial Intelligence",
    "Machine Learning"
]

embeddings = create_embeddings(text)

print(type(embeddings))
