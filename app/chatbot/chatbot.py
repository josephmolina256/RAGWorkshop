from hugchat import hugchat
from hugchat.login import Login

from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer

import os
from dotenv import load_dotenv

# Reference: https://github.com/Soulter/hugging-chat-api

class RAGAgent:
    def __init__(self):
        """Initialize the HuggingChatWrapper class and load environment variables."""
        ...

    def retrieve_similar_question(self, user_query, qa_embeddings, threshold=0.3):
        """Finds the most similar question from the stored Q&A pairs and returns the embedding vector value, question, and answer."""
        ...
