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
import os
import re

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")


class CollectionStatus(Enum):
    COLLECTION_CREATED = auto()
    COLLECTION_EXISTS = auto()


def ensure_collection(client: chromadb.ClientAPI, collection_name) -> tuple[CollectionStatus, Optional[Collection]]:
    demo_collection = "demo"

    try:
        collection = client.create_collection(name=collection_name)
        print(f"Collection '{collection_name}' created successfully.")
        return CollectionStatus.COLLECTION_CREATED, collection
    except Exception as e:
        print(f"Failed to create collection '{collection_name}': {e}")
        raise e


def clean_text(raw_text: str) -> str:
    # Clean up the text to remove extra spaces and line breaks
    cleaned_text = raw_text.replace("\n", " ")
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)
    return cleaned_text


def get_chunks(text: str, max_words: int = 150) -> list[tuple[str, int]]:
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
    files_directory = Path("./db_files_md")  # Folder containing markdown files

    if not db_directory.exists():
        db_directory.mkdir()

    if not files_directory.exists():
        print("DB files were not copied! Abort.")
        sys.exit(1)

    chroma_client = chromadb.PersistentClient(path=str(db_directory))

    # Define the groups of files (based on your example)
    file_groups = [
        ["E1080.md"],  # First collection should come from E1080_md
        ["E1050.md"],  # Second collection should come from E1051_md
        ["S1012.md"],  # Third collection should come from E1020_md
        ["ScaleOut.md"],  # Fourth collection should come from E1010_md
    ]

    # Iterate over the file groups and create a collection for each
    for i, group in enumerate(file_groups):
        print("Adding collection group", i + 1)
        collection_name = f"collection_group_{i + 1}"
        collection_status, collection = ensure_collection(chroma_client, collection_name)

        if collection_status == CollectionStatus.COLLECTION_EXISTS:
            print(f"Collection '{collection_name}' already exists. Skipping file insertion.")
        else:
            print(f"Creating collection '{collection_name}' and inserting documents.")
            for file_name in group:
                document_path = files_directory / file_name
                if document_path.exists():
                    insert_document(document_path, collection)
                    print(f"Inserted {file_name} into {collection_name}")

                else:
                    print(f"File {file_name} not found!")
                time.sleep(5)

    # Final collection with all the markdown files in the directory
    final_collection_name = "final_collection_all_files"
    collection_status, collection = ensure_collection(chroma_client, final_collection_name)

    if collection_status == CollectionStatus.COLLECTION_EXISTS:
        print(f"Collection '{final_collection_name}' already exists. Skipping file insertion.")
    else:
        print(f"Creating collection '{final_collection_name}' and inserting all documents.")
        for document_path in files_directory.glob("*.md"):  # Insert all .md files
            insert_document(document_path, collection)
            print(f"Inserted {document_path.name} into {final_collection_name}")
            time.sleep(5)

    print("Setup completed.")

    # Example query for testing
    result = collection.query(
        query_texts=["What is IBM POWER"],
        n_results=5,
        include=["documents"]
    )
    print(result)


if __name__ == "__main__":
    main()
                                                       
