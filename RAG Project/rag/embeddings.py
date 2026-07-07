from rag.client import client
import numpy as np
from huggingface_hub import InferenceClient

from config import HF_API_KEY

client = InferenceClient(
    provider = 'hf-inference',
    api_key=HF_API_KEY
)

MODEL = "BAAI/bge-small-en-v1.5"

def create_embeddings(texts):
    embeddings = client.feature_extraction(
        texts,
        model=MODEL
    )

    return np.array(embeddings, dtype=np.float32)




