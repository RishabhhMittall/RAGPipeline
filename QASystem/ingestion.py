from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv
from QASystem.utils import pinecone_config

def ingest(document_store):

	#creating a pipeline object
	indexing = Pipeline()

	#adding the components in pipeline
	indexing.add_component("converter", PyPDFToDocument())
	# indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=1))
	indexing.add_component("splitter", DocumentSplitter(split_by="word", split_length=150, split_overlap=20))

	indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
	indexing.add_component("writer", DocumentWriter(document_store))

	#conecting all the components of pipeline
	indexing.connect("converter", "splitter")
	indexing.connect("splitter", "embedder")
	indexing.connect("embedder", "writer")

	#storing the data as a embedding in the database
	indexing.run({"converter": {"sources": [Path("C:\\Users\\risha\\OneDrive\\Desktop\\RAGPipelineHaystack\\data\\Retrieval-Augmented-Generation-for-NLP.pdf")]}})
 
 
if __name__ == "__main__":
    #loading the environment variable
    '''load_dotenv()
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    
    print("Import Successfully")'''
    document_store=pinecone_config()
    
    ingest(document_store)