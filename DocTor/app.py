from rag.pipeline import RAGPipeline

pipeline = RAGPipeline()

pipeline.build_index(
    "/workspaces/codespaces-blank/RAG Project/Documents/UpdatedResume2.pdf"
)

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = pipeline.ask(question)

    print("\nAnswer:\n")

    print(answer)
