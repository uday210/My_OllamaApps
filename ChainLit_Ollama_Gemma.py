import ollama 
import chainlit as ct

@ct.on_message
async def on_message(message: ct.Message):

    response = ollama.chat(
        model="gemma3",
        messages=[
            {
                'role':'user',
                'content':message.content
            }
        ]
    )

    await ct.Message(content=response['message']['content']).send()


@ct.on_chat_start
async def start():
    await ct.Message(content="Hello Gemma, how are you? give me a mean plan").send()
