from hugchat import hugchat
from hugchat.login import Login

from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer

import os
import json
from dotenv import load_dotenv

class RAGAgent:
    def __init__(self):
        """Initialize the HuggingChatWrapper class and load environment variables."""
        # Load environment variables
        load_dotenv()

        # Fetch environment variables
        self.__email = os.getenv("HUGGINGFACE_EMAIL")
        self.__password = os.getenv("HUGGINGFACE_PASSWORD")

        if not self.__email or not self.__password:
            raise ValueError("Missing HUGGINGFACE_EMAIL or HUGGINGFACE_PASSWORD in environment variables.")

        sign = Login(self.__email, self.__password)
        cookies = sign.login()
        self.chatbot_instance = hugchat.ChatBot(
                    cookies=cookies.get_dict(),
                    default_llm="meta-llama/Llama-3.3-70B-Instruct"
                )
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        print("initialized NEW RAGAgent")

    def retrieve_similar_question(self, user_query, qa_embeddings, threshold=0.3):
        """Finds the most similar question from the stored Q&A pairs and returns the embedding vector value, question, and answer."""
        user_embedding = self.embedding_model.encode(user_query)

        best_match = None
        best_score = float("inf")

        for embedding_item in qa_embeddings:
            score = cosine(user_embedding, embedding_item["embedding"])
            if score < best_score:  # Lower cosine distance = higher similarity
                best_score = score
                best_match = embedding_item
                print(best_score, best_match["qa_item"])

        if best_score < threshold:
            return best_match

        return None
