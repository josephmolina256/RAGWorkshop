import os
from dotenv import load_dotenv
from hugchat import hugchat
from hugchat.login import Login


class HuggingChatWrapper:
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
        self.chatbot_instance = self._chatbot_instance = hugchat.ChatBot(
                    cookies=cookies.get_dict(),
                    default_llm="meta-llama/Llama-3.3-70B-Instruct"
                )
        print("initialized NEW HuggingChatWrapper")

