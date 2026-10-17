from langchain_openai import OpenAi
from dotenv import load_dotenv

load_dotenv()

llm = OpenAi(model_name="gpt-3.5-turbo-instruct")

result = llm.invoke("Write a short poem about the beauty of nature.")

print(result)