print("Checking NumPy...")
import numpy as np
print("✓ NumPy OK")

print("Checking FAISS...")
import faiss
print("✓ FAISS OK")

print("Checking Hugging Face...")
from huggingface_hub import InferenceClient
print("✓ Hugging Face OK")

print("Checking OpenAI SDK...")
from openai import OpenAI
print("✓ OpenAI SDK OK")

print("\nEnvironment is ready 🚀")