<!-- 
TRACKING FILE: UPDATED AS TASKS ARE COMPLETED.
-->

# Project Tasks

- [x] Task 1: Exploratory Data Analysis and Data Preprocessing
  - [x] Load the full CFPB complaint dataset
  - [x] Filter for: Credit card, Personal loan, Savings account, Money transfers
  - [x] Remove records with empty narratives
  - [x] Clean text narratives
  - [x] Save filtered data to data/filtered_complaints.csv
  - [x] Create notebook/script for EDA
  - [x] Write summary in report

- [x] Task 2: Text Chunking, Embedding, and Vector Store Indexing
  - [x] Create stratified sample (12,000 records)
  - [x] Implement text chunking strategy (500 chars, 50 overlap)
  - [x] Choose embedding model (all-MiniLM-L6-v2)
  - [x] Generate embeddings and create vector store (FAISS)
  - [x] Store metadata (product, company, state, etc.)
  - [x] Save vector store to vector_store/

- [x] Task 3: Building the RAG Core Logic and Evaluation
  - [x] Load pre-built vector store
  - [x] Implement Retriever
  - [x] Design Prompt Template
  - [x] Implement Generator
  - [x] Perform Qualitative Evaluation
  - [x] Create evaluation table

- [x] Task 4: Creating an Interactive Chat Interface
  - [x] Build Gradio app
  - [x] Implement text input, submit, answer display
  - [x] Display sources
  - [x] Add example queries
  - [x] Implement chat history
  - [x] Add logging for interactions
  - [x] Error handling

