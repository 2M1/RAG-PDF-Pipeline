import chromadb
from chromadb import Client
from sentence_transformers import SentenceTransformer
from pathlib import Path
import os
 
 
base_directory = Path(os.getcwd()) 
 
database = base_directory / "db" 
# Initialize Chroma client and collection
chroma_client = chromadb.PersistentClient(path="./db")   # Change path accordingly
collection = chroma_client.get_collection(name="demo") 
 
results = collection.query( 
    query_texts=["What are the new features of the"], 
    n_results=5, 
    include=["documents"] 
) 
 
print(results) 
 
