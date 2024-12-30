RAG Pipeline for RedBooks.

RedBooks are already converted to markdown files with the python library docling.

To use this project you need to install ChromaDB and llama-cpp-python.

First execute chromaDB_md.py. This will create one Vector database in the folder /db with 5 collections.
Each collection comes from 1 markdown file. The last collection has the embedding from all of the markdown files.

To use the LLM, you need to change the model:path in run_model.py to your gguf model.

ToDOs: 

- Streaming -> Done
- Multiple Vector Databases -> Done
- Make max tokens larger
- Get better output quality (Prompt Engineering?)
