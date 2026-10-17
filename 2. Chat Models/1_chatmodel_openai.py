from langchain_openai import ChatOpenAi
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAi(chat_model="gpt-4")

result = chat_model.invoke("Write a short poem about the beauty of nature.")

print(result)