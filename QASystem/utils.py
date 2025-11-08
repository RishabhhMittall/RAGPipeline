from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.utils.auth import Secret   # ✅ import Secret for secure API handling
import os
from dotenv import load_dotenv

load_dotenv()

# Load keys from .env
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Optional: set as environment variables (helps other libs like Transformers)
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['HF_API_TOKEN'] = HF_TOKEN

print("Import Successfully")

def pinecone_config():
    """Configure Pinecone document store for Haystack."""
    document_store = PineconeDocumentStore(
        api_key=Secret.from_token(PINECONE_API_KEY),  # ✅ wrap inside Secret
        index="default",                              # your Pinecone index name
        namespace="default",                          # optional logical grouping
        dimension=768                                 # depends on your embedding model
    )
    return document_store
