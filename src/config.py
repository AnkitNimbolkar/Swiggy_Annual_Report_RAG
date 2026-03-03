import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_PATH = os.path.join(BASE_DIR, "data", "Swiggy-Annual-Report-FY-2024-25.pdf")
CHROMA_DIR = os.path.join(BASE_DIR, "artifacts", "chroma_swiggy")

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# Embeddings
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# LLM via Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

LLM_TEMPERATURE = 0.1
LLM_MAX_NEW_TOKENS = 512