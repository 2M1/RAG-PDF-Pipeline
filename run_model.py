import gradio as gr
import chromadb
from llama_cpp import Llama
import os
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import time

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")

# Initialize LLaMA model with llama-cpp-python (local model)
llama_model_path = "model:path"  # Path to your LLaMA model
llama = Llama(model_path=llama_model_path, n_ctx=0)

#model = SentenceTransformer('all-mpnet-base-v2')
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

# Function to retrieve relevant documents from ChromaDB
def retrieve_documents(query, collection_name, top_k=3):
 
    collection = chroma_client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
    
    #query_embedding = model.encode([query])[0]

    # Perform similarity search with ChromaDB
    results = collection.query(query_texts=[query], n_results=top_k)
    
    # Extract the documents
    retrieved_documents = results["documents"]
    return retrieved_documents

# Function to generate response with LLaMA model using llama-cpp-python
def generate_response(query, collection_name, use_context=True):
    if use_context:
        
        documents = retrieve_documents(query, collection_name) if use_context else []
        
        print("documents")
        print(documents)
        # Combine the query with the retrieved documents as context
        flat_documents = [item for sublist in documents for item in sublist]
        context = "\n".join(flat_documents)
        input_text = f"""
        Instructions: Compose a comprehensive reply to the query using the search results given. If the search results mention multiple subjects with the same name, create separate answers for each. Only include information found in the results and don't add any additional information. Make sure the answer is correct and don't output false content. If the text does not relate to the query, simply state 'Found Nothing'. Ignore outlier search results which has nothing to do with the question. Only answer what is asked.

        Query:
        {context}

        Question:
        {query}

        Answer:
        """

        print(input_text)
    else:
        # Use only the query without context
        input_text = f"Query: {query}\nAnswer:"

    cmData = ""
    # Generate a response from the LLaMA model
    for output in llama(input_text, max_tokens=4096, stream=True):
        print(output)
        #time.sleep(1)
        if (output['choices'][0]['text'] == '\n'):
            break
        elif (output['choices'][0]['text'] == ' \n\n'):
            break
        else:
            data = output['choices'][0]['text']
            cmData += data
            yield cmData

# Create Gradio UI
def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Chatbot for Openshift and POWER Systems based on the IBM RedBooks")
        gr.Markdown("This is a Chatbot which has context from the Openshift RedBook for POWER and the Systems itself. If you do not want to use any context, then switch off the box under Use Context (RAG).")
        gr.Markdown("If this is switched off, then you are basically using a normal Chatbot without any additional context")

        with gr.Row():
            query_input = gr.Textbox(label="Enter your query", placeholder="What would you like to know?")

        with gr.Row():
            use_context_toggle = gr.Checkbox(label="Use Context (RAG)", value=True)
        
        with gr.Row():
            # Dropdown for selecting the file from 5 options
            file_selector = gr.Dropdown(
                label="About which POWER Topic do you want to have Information?",
                choices=["E1080", "E1050", "S1012", "ScaleOut", "Openshift"],  # List of your file names
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
