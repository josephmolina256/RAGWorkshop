import chainlit as cl

from components.chatbot.chatbot_SOLUTION import HuggingChatWrapper

ChatWrapper = HuggingChatWrapper()

@cl.on_message
async def main(message: cl.Message):
    res = ChatWrapper.chatbot_instance.chat(message.content).wait_until_done()
    await cl.Message(
        content=res,
    ).send()
