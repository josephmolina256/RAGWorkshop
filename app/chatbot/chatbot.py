from hugchat import hugchat
from hugchat.login import Login

from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer
import numpy as np

import os
import json
from dotenv import load_dotenv

# Reference: https://github.com/Soulter/hugging-chat-api
# Create account on https://huggingface.co/
# Login https://huggingface.co/chat/

class RAGAgent:
    def __init__(self):
        """Initialize the HuggingChatWrapper class and load environment variables."""
        ...

    def retrieve_similar_question(self, user_query):
        """Finds the most similar question from the stored Q&A pairs and returns the embedding vector value, question, and answer."""
        ...

