import gradio as gr
import chromadb
from llama_cpp import Llama
import os
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")

# Initialize LLaMA model with llama-cpp-python (local model)
llama_model_path = ""  # Path to your LLaMA model
llama = Llama(model_path=llama_model_path)

model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to retrieve relevant documents from ChromaDB
def retrieve_documents(query, collection_name, top_k=1):
 
    collection = chroma_client.get_collection(name=collection_name)
    
    #query_embedding = model.encode([query])[0]

    # Perform similarity search with ChromaDB
    results = collection.query(query_texts=[query], n_results=top_k)
    
    # Extract the documents
    retrieved_documents = results["documents"]
    return retrieved_documents

# Function to generate response with LLaMA model using llama-cpp-python
def generate_response(query, collection_name, use_context=True):
    if use_context:
        
        final_collection_name = ""
        if (collection_name == "E1080"):
            print("using E1080")
            final_collection_name = "collection_group_1"
        elif (collection_name == "E1050"):
            print("using E1050")
            final_collection_name = "collection_group_2"
        elif (collection_name == "S1012"):
            print("using S1012")
            final_collection_name = "collection_group_3"
        elif (collection_name == "Scale Out"):
            print("using Scale out")
            final_collection_name = "collection_group_4"
        else:
            print("using all")
            final_collection_name = "final_collection_all_files"
        documents = retrieve_documents(query, final_collection_name) if use_context else []
        
        print("documents")
        print(documents)
        # Combine the query with the retrieved documents as context
        flat_documents = [item for sublist in documents for item in sublist]
        context = "\n".join(flat_documents)
        input_text = f"Here is some relevant information:\n{context}\n\nBased on this information, please answer the following question:\n{query}\nAnswer:"
        print(input_text)
    else:
        # Use only the query without context
        input_text = f"Query: {query}\nAnswer:"

    cmData = ""
    # Generate a response from the LLaMA model
    for output in llama(input_text, max_tokens=9600, stream=True):
        data = output['choices'][0]['text']
        cmData += data
        yield cmData

# Create Gradio UI
def main():
    with gr.Blocks() as demo:
        gr.Markdown("# RAG Pipeline with Toggleable Context")

        with gr.Row():
            query_input = gr.Textbox(label="Enter your query", placeholder="What would you like to know?")

        with gr.Row():
            use_context_toggle = gr.Checkbox(label="Use Context (RAG)", value=True)
        
        with gr.Row():
            # Dropdown for selecting the file from 5 options
            file_selector = gr.Dropdown(
                label="About which POWER System do you want to have Information?",
                choices=["E1080", "E1050", "S1012", "Scale Out", "All Systems"],  # List of your file names
                value="All Systems"  # Default selection
            )
        
        with gr.Row():
            submit_button = gr.Button("Submit")

        with gr.Row():
            response_output = gr.Textbox(label="Response", placeholder="Response will appear here.")

        # Event handling
        submit_button.click(fn=generate_response, inputs=[query_input, file_selector, use_context_toggle], outputs=[response_output])

    demo.launch(server_name = "0.0.0.0", enable_queue=True)

if __name__ == "__main__":
    main()
