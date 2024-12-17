import chromadb
from llama_cpp import Llama
import os
import torch

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.get_collection(name="demo")

# Initialize LLaMA model with llama-cpp-python (local model)
llama_model_path = "./Meta-Llama-3-8B.Q8_0.gguf"  # Path to your LLaMA model
llama = Llama(model_path=llama_model_path)

# Function to retrieve relevant documents from ChromaDB
def retrieve_documents(query, top_k=2):
    # Perform similarity search with ChromaDB
    results = collection.query(query_texts=[query], n_results=top_k)
    
    # Extract the documents
    retrieved_documents = results["documents"]
    return retrieved_documents

# Function to generate response with LLaMA model using llama-cpp-python
def generate_response(query, documents):
    # Combine the query with the retrieved documents as context
    flat_documents = [item for sublist in documents for item in sublist]
    print("Flat documents")
    print(flat_documents)
    context = "\n".join(flat_documents)
    input_text = f"Query: {query}\nContext: {context}\nAnswer:"
    
    # Generate a response from the LLaMA model
    response = llama(input_text, max_tokens=1200)
    print(response)
    print(response['choices'])
    text = response['choices'][0]['text']
    return text

# Main function to run the RAG pipeline
def rag_pipeline(query):
    # Step 1: Retrieve relevant documents from ChromaDB
    retrieved_documents = retrieve_documents(query)
    print("retreived documents")
    print(retrieved_documents)
    
    # Step 2: Generate response with LLaMA
    response = generate_response(query, retrieved_documents)
    
    return response

# Example usage
query = "What are the main characteristics of the E1050?"
response = rag_pipeline(query)
print(response)
