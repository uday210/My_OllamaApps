import ollama 

response = ollama.chat(
    model="gemma3",
    messages=[
        {
            'role':'user',
            'content':'Hello Gemma, how are you? give me a mean plan '
        }
    ]
)

print(response['message']['content'])