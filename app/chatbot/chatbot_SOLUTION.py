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
        load_dotenv()

        # Use dotenv to load environment variables from .env file
        EMAIL = os.environ.get("HUGGINGFACE_EMAIL") 
        PASSWD = os.environ.get("HUGGINGFACE_PASSWD")


        cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
        sign = Login(EMAIL, PASSWD)
        cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

        self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

        with open("data/output/ftp_data_SOLUTION.json", "r") as file:
            self.database = json.load(file)

    def retrieve_similar_question(self, user_query):
        """Finds the most similar question from the stored Q&A pairs and returns the embedding vector value, question, and answer."""
        input_embedding = self.embedding_model.encode(user_query)

        best_match = None
        best_score = float("inf")
        for data in self.database:
            score = cosine(input_embedding, np.array(data["embedding"]))
            print(f"Cosine distance between '{user_query}' and '{data['text']}': {score}")
            if score < best_score and score < 0.4:
                best_score = score
                best_match = data["text"]

        return best_match
    
    def OPTIONAL_login(self, email, password):
        EMAIL = email 
        PASSWD = password

        cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
        sign = Login(EMAIL, PASSWD)
        cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

        self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
