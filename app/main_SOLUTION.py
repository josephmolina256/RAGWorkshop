import chainlit as cl # https://docs.chainlit.io/get-started/pure-python 

from chatbot.chatbot_SOLUTION import RAGAgent

chatbot = RAGAgent()

@cl.on_message
async def main(message: cl.Message):

    similar_content = chatbot.retrieve_similar_question(message.content)

    if similar_content:
        input_to_chatbot = (
            f"Relevant Information: {similar_content}\n"
            f"User asked: {message.content}\n"
            f"Now answer the question based on the information provided.\n\n"
        )
    else: 
        input_to_chatbot = message.content

    print(input_to_chatbot)


    await cl.Message(
        content=chatbot.chatbot.chat(input_to_chatbot).wait_until_done(),
    ).send()
