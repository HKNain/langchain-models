import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of India?"
        }
    ],
    max_tokens=100,
)

print(completion.choices[0].message.content)