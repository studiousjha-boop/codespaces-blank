from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import create_embeddings
from rag.vector_store import create_index
from rag.retriever import retrieve
from rag.llm_service import generate_answer


class RAGPipeline:

    def __init__(self):
        self.index = None
        self.chunks = None

    def build_index(self, pdf_path):
        
        text = load_pdf(pdf_path)

        self.chunks = chunk_text(text)

        embeddings = create_embeddings(self.chunks)

        self.index = create_index(embeddings)


    def ask(self, question):
        
        retrieved_chunks = retrieve(
            question,
            self.index,
            self.chunks    
        )

        return generate_answer(
            question,
            retrieved_chunks
        )
    

