import gradio as gr
import chromadb
from llama_cpp import Llama
import os

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.get_collection(name="demo")

# Initialize LLaMA model with llama-cpp-python (local model)
llama_model_path = "./llama-2-7b-chat.Q8_0.gguf"  # Path to your LLaMA model
llama = Llama(model_path=llama_model_path)

# Function to retrieve relevant documents from ChromaDB
def retrieve_documents(query, top_k=2):
    # Perform similarity search with ChromaDB
    results = collection.query(query_texts=[query], n_results=top_k)
    
    # Extract the documents
    retrieved_documents = results["documents"]
    return retrieved_documents

# Function to generate response with LLaMA model using llama-cpp-python
def generate_response(query, use_context=True):
    if use_context:

        documents = retrieve_documents(query) if use_context else []

        # Combine the query with the retrieved documents as context
        flat_documents = [item for sublist in documents for item in sublist]
        context = "\n".join(flat_documents)
        input_text = f"Query: {query}\nContext: {context}\nAnswer:"
    else:
        # Use only the query without context
        input_text = f"Query: {query}\nAnswer:"

    cmData = ""
    # Generate a response from the LLaMA model
    for output in llama(input_text, max_tokens=4200, stream=True):
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
            submit_button = gr.Button("Submit")

        with gr.Row():
            response_output = gr.Textbox(label="Response", placeholder="Response will appear here.")

        # Event handling
        submit_button.click(fn=generate_response, inputs=[query_input, use_context_toggle], outputs=[response_output])

    demo.launch()

if __name__ == "__main__":
    main()
