from rag.client import client
from settings import LLM_MODEL

def build_prompt(question, chunks):

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, reply exactly:
"I couldn't find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""
    
    return prompt


def generate_answer(question, chunks):


    prompt = build_prompt(question, chunks)

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
           { 
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content
