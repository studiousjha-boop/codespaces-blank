def build_prompt(question, chunks):
    context = "\n\n".join(chunks)

    prompt = f"""
    You are a helpful AI assistant.

    Answer ONLY using the context below.

    If the answer is not found, reply:
    "I couldn't find that information in the document."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    return prompt
