from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
   "Kathmandu is the capital of Nepal",
    "Hetauda is the capital of Bagmati Province",
    "Paris is the capital of France"
]


vector = embedding.embed_documents(documents)

print(str(vector))