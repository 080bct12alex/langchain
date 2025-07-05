from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Kathmandu is the capital of Nepal",
    "Hetauda is the capital of Bagmati Province",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))