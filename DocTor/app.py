from rag.pipeline import RAGPipeline

try:
    pipeline = RAGPipeline()

    pipeline.build_index(
        "/workspaces/codespaces-blank/DocTor/Documents/UpdatedResume2.pdf"
    )

    while True:
        question = input("\nAsk: ")
        if question.lower() == "exit":
            break
        answer = pipeline.ask(question)
        print("\nAnswer:\n")
        print(answer)
except KeyboardInterrupt:
    print("\nExiting...")
except EOFError:
    print("\nInput closed. Exiting...")
