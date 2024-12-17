import os
import re
import sys
from enum import auto
from enum import Enum
from pathlib import Path
from typing import Optional
import chromadb
from chromadb import Collection
from pypdf import PdfReader, PageObject


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
    cleaned_text = raw_text.replace("\n", " ")
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)
    return cleaned_text


def get_chunks(pages: list[PageObject], max_words: int = 150) -> list[tuple[str, int]]:
    text_tokens = [(clean_text(page.extract_text()).split(" "), page.page_number) for page in pages]
    chunks = []

    for idx, (words, page_number) in enumerate(text_tokens):
        for i in range(0, len(words), max_words):
            chunk = words[i:i + max_words]
            if (i + max_words) > len(words) and (len(chunk) < max_words) and (
                    len(text_tokens) != (idx + 1)):
                next_page = text_tokens[idx + 1]
                text_tokens[idx + 1] = (chunk + next_page[0], next_page[1])
                continue
            chunk = " ".join(chunk).strip()
            chunk = f'[Page no. {page_number}]' + ' ' + '"' + chunk + '"'
            chunks.append((chunk, page_number))
    print("CHUNKS")
    print(chunks)
    return chunks


def insert_document(document_path: Path, collection: Collection) -> None:
    document_reader = PdfReader(document_path)
    document_name = document_path.stem.replace(" ", "-").replace("_", "-")
    pages = document_reader.pages

    document_chunks = []
    document_ids = []

    chunks = get_chunks(pages)
    for chunk_index, (chunk, page_number) in enumerate(chunks):
        document_ids.append(f"{document_name}_p{page_number}-{chunk_index}")
        document_chunks.append(chunk)

    # Add documents to the collection
    collection.add(
        documents=document_chunks,
        ids=document_ids,
    )


def main() -> None:
    base_directory = Path(os.getcwd())
    db_directory = base_directory / "db"
    files_directory = base_directory / "db_files_pdf"

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
    for document_path in files_directory.glob("*.pdf"):
        insert_document(document_path, collection)

    print("Setup completed.")


if __name__ == "__main__":
    main()
