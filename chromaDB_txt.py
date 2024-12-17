import os
import re
import chromadb
from chromadb import Collection
from pathlib import Path

# Initialize Chroma client
chroma_client = chromadb.PersistentClient(path="./db")  # Change path accordingly
collection = chroma_client.get_or_create_collection(name="demo")

def load_document(file_path: Path) -> str:
    """Load the content of a single file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def clean_text(text: str) -> str:
    """Clean and preprocess the text (remove extra spaces, etc.)."""
    text = text.replace("\n", " ").strip()
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
    return text

def insert_files_as_chunks(folder_path: Path, collection: Collection):
    """Read all .txt files in the folder and add each file as a chunk to ChromaDB."""
    document_ids = []
    document_chunks = []
    
    for file_path in folder_path.glob("*.txt"):
        # Load and clean the document
        document_text = load_document(file_path)
        cleaned_text = clean_text(document_text)
        
        # Use the file name (without extension) as the document ID
        document_id = file_path.stem
        
        # Append to lists
        document_ids.append(document_id)
        document_chunks.append(cleaned_text)

    
    print("document id")
    print(document_ids)
    
    # Add all files as chunks to the ChromaDB collection
    collection.add(
        documents=document_chunks,
        ids=document_ids,
    )
    print(f"Inserted {len(document_ids)} documents into the collection.")

def main():
    # Path to your folder containing .txt files
    folder_path = Path("./db_files_txt/")  # Replace with your actual folder path
    
    # Insert all .txt files as chunks into ChromaDB
    insert_files_as_chunks(folder_path, collection)
    
    print("All text files loaded into ChromaDB.")

if __name__ == "__main__":
    main()
