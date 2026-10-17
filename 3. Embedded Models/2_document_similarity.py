from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    dimension=300
)

documents = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo.",
    "The capital of Germany is Berlin.",
    "The capital of Canada is Ottawa."
]

query = "Tell me about India Capital"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

cosine_score = cosine_similarity([query_embedding], doc_embeddings)

index, cosine_score = sorted(list(enumerate(cosine_score[0])), key=lambda x: x[1])[-1]

print(documents[index])
print("similarity_score:", cosine_score)