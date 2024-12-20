import os
import re
import sys
from enum import auto
from enum import Enum
from pathlib import Path
from typing import Optional
import chromadb
from chromadb.utils import embedding_functions
from chromadb import Collection
from transformers import AutoTokenizer, AutoModel
import torch
import psutil
import time

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")


class CollectionStatus(Enum):
    COLLECTION_CREATED = auto()
    COLLECTION_EXISTS = auto()


def ensure_collection(client: chromadb.ClientAPI) -> tuple[CollectionStatus, Optional[Collection]]:
    demo_collection = "demo"

    try:
        # Attempt to retrieve the collection
        collection = client.get_collection(name=demo_collection)
        return CollectionStatus.COLLECTION_EXISTS, collection
    except chromadb.errors.InvalidCollectionException:
        # If collection doesn't exist, create a new one
        print(f"Collection '{demo_collection}' does not exist. Creating a new one.")
        collection = client.get_or_create_collection(name=demo_collection)
        return CollectionStatus.COLLECTION_CREATED, collection


def clean_text(raw_text: str) -> str:
    # Clean up the text to remove extra spaces and line breaks
    cleaned_text = raw_text.replace("\n", " ")
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)
    return cleaned_text


def get_chunks(text: str, max_words: int = 50) -> list[tuple[str, int]]:
    words = clean_text(text).split(" ")
    chunks = []
    # Split the text into chunks of max_words length
    for i in range(0, len(words), max_words):
        chunk = words[i:i + max_words]
        chunk_text = " ".join(chunk).strip()
        chunks.append((chunk_text, i // max_words))
    return chunks


def insert_document(document_path: Path, collection: Collection) -> None:
    """
    Reads a markdown file, splits it into chunks, generates embeddings,
    and inserts the chunks into a ChromaDB collection.
    """
    # Read the markdown file content
    with open(document_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    document_name = document_path.stem.replace(" ", "-").replace("_", "-")

    # Get chunks of text from the markdown content
    chunks = get_chunks(markdown_content)
    document_chunks = []
    document_ids = []
    embeddings = []

    for chunk_index, (chunk, _) in enumerate(chunks):
        # Generate embedding for the chunk

        # Append results
        document_ids.append(f"{document_name}_chunk{chunk_index}")
        document_chunks.append(chunk)

    print("Adding chunks to collection:")
    #print(document_chunks)

    # Add documents with embeddings to the ChromaDB collection
    batch_size = len(document_chunks) // 100  # Calculate 10% of chunks
    if batch_size == 0:  # Handle small input where 10% is less than 1
        batch_size = 1

    # Iterate through document_chunks in batches
    for i in range(0, len(document_chunks), batch_size):
        batch_chunks = document_chunks[i:i + batch_size]
        batch_ids = document_ids[i:i + batch_size]
        print(batch_ids)

        print(f"Before batch {i}, Memory Usage: {psutil.virtual_memory().percent}%")
        try:
            collection.add(
                documents=batch_chunks,
                ids=batch_ids
            )
        except Exception as e:
            print(f"Error occurred: {e}")
        print(f"After batch {i}, Memory Usage: {psutil.virtual_memory().percent}%")



def main() -> None:
    base_directory = Path(os.getcwd())
    db_directory = Path("./db")
    files_directory = Path("./db_files_md")  # Change the folder name to "db_files_md"

    if not db_directory.exists():
        db_directory.mkdir()

    if not files_directory.exists():
        print("DB files were not copied! Abort.")
        sys.exit(1)

    chroma_client = chromadb.PersistentClient(path=str(db_directory))
    collection_status, collection = ensure_collection(chroma_client)

    # If collection already exists, skip loading files
    if collection_status == CollectionStatus.COLLECTION_EXISTS:
        print("Collection already exists. No new files are loaded.")
        sys.exit(0)

    # Insert documents into collection
    for document_path in files_directory.glob("*.md"):  # Searching for markdown files
        insert_document(document_path, collection)
        print("Finished inserting")
        time.sleep(5)

    print("Setup completed.")

    result = collection.query( 
        query_texts=["What is IBM POWER"], 
        n_results=5, 
        include=["documents"] 
    ) 
    print(result)


if __name__ == "__main__":
    main()
