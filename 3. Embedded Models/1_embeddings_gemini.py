from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

# Convert a single text into an embedding vector
text = "What is the capital of India?"
vector = embeddings.embed_query(text)

print("Embedding vector:")
print(vector)

print("\nVector dimensions:", len(vector))