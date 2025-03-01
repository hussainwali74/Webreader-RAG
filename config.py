import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Config
PAGE_CONFIG = {
    "layout": "wide",
    "page_title": "CrawlerAI Chatbot",
    "page_icon": "🤖"
}

# LLM Config
LLM_CONFIG = {
    "model_name": "gpt-4o-mini",
    "temperature": 0.3,
    "max_tokens": 1000
}

# Embedding Config
EMBEDDING_CONFIG = {
    "chunk_size": 1000,
    "chunk_overlap": 100,
    "model": "text-embedding-3-large"
}

# File paths
FAISS_INDEX_PATH = "faiss_index"
OUTPUT_MD_PATH = "output.md"
CHAT_HISTORY_PATH = "chat_history.txt"
