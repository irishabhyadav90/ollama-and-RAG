import ollama
import json

# models = ollama.list()

# res = ollama.chat(
#     model="gemma3:4b",
#     messages=[{
#         "role": "user",
#         "content": "Give me a joke about AI. in less than 20 words."
#     }],
#     stream= True

# )

# for chunk in res:
#     if chunk.message and chunk.message.content:
#         print(chunk.message.content, end='', flush=True)

modelfile = """
FROM gemma3:4b
SYSTEM you are a helpful assistant. your name is sheikh, you know everything about Middle east history, culture, and politics.
PARAMETER temperature 0.1
"""

ollama.create(model="middle-east", from_="gemma3:4b", system="you are a helpful assistant. your name is sheikh, you know everything about Middle east history, culture, and politics.", parameters={"temperature": 0.1})
res = ollama.generate(model="middle-east", prompt="What is your name?", stream=False)

ollama.delete(model="middle-east")
ollama.delete(model="ranchordas:latest")