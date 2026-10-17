from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(chat_model="claude-3-5-sonnet-28241022")

result = chat_model.invoke("Write a short poem about the beauty of nature.")

print(result.content)