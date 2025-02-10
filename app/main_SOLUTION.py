import chainlit as cl
import numpy as np
from chatbot.chatbot_SOLUTION import RAGAgent

import json

rag_agent = RAGAgent()

def load_embedded_qa_data(file_path="data/output/embedded_data.json"):
    try:
        with open(file_path, "r") as file:
            qa_embeddings = json.load(file)

        # Convert embeddings back to NumPy arrays
        for item in qa_embeddings:
            item["embedding"] = np.array(item["embedding"])  # Convert list to ndarray

        return qa_embeddings  # Return list of dicts with NumPy embeddings
    
    except Exception as e:
        print(f"Error: {e}")
        return None  # Failure

qa_embeddings = load_embedded_qa_data()

@cl.on_message
async def main(message: cl.Message):    
    additional_context_with_embedding = rag_agent.retrieve_similar_question(
        message.content,
        qa_embeddings
    )

    if additional_context_with_embedding:
        chatbot_input = (
            f"User: {message.content}\n"
            f"Here is some additional context: {additional_context_with_embedding["qa_item"]}\n"
            "Now generate the best response based on this information.\n\n"
        )
    else:
        chatbot_input = (
                    f"User: {message.content}\n"
                )
    
    msg = cl.Message(content="")

    stream = rag_agent.chatbot_instance.chat(chatbot_input)  # No await

    for part in stream:
        # print("Stream part:", part)  # Debug output to see its structure

        # Try to extract the token based on its actual structure
        if isinstance(part, dict) and "token" in part:
            token = part["token"]  # Extract token from dictionary
            await msg.stream_token(token)  # Send token to Chainlit

    await msg.update()  # Final update


