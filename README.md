# Intelligent Complaint Analysis for Financial Services

This project implements a Retrieval-Augmented Generation (RAG) system for intelligent analysis of consumer financial complaints. It leverages the Consumer Financial Protection Bureau (CFPB) dataset to provide a chatbot interface that can understand and answer questions about consumer complaints.

## Project Structure

```
├── data/               # Data directory (raw and processed)
├── notebooks/          # Jupyter notebooks for analysis and experimentation
├── report/             # Generated reports, images, and statistics
├── src/                # Source code directory
│   ├── data_preprocessing.py   # Task 1: Data cleaning and filtering
│   ├── eda_analysis.py         # Task 1: Exploratory Data Analysis
│   ├── sampling.py             # Task 2: Stratified sampling
│   ├── chunking.py             # Task 2: Text chunking
│   ├── embedding.py            # Task 2: Embedding generation
│   └── vector_store_builder.py # Task 2: FAISS vector store creation
├── vector_store/       # Directory for persisted vector stores
└── requirements.txt    # Project dependencies
```

## Tasks Overview

### Task 1: Data Preprocessing and EDA
**Objective**: Prepare the raw dataset for analysis and understand its characteristics.
- **Data Filtering**: Processed over 9.6M records to extract ~82,000 relevant complaints across 4 target product categories:
  - Credit card
  - Personal loan
  - Savings account
  - Money transfers
- **Exploratory Analysis**: Analyzed product distribution, narrative lengths, and temporal patterns.
- **Output**: Cleaned dataset `data/processed/filtered_complaints.csv` and EDA report.

### Task 2: Text Chunking, Embedding, and Vector Store
**Objective**: Create a semantic search engine using vector embeddings.
- **Stratified Sampling**: Created a representative sample of 12,000 complaints to ensure proportional product representation.
- **Text Chunking**: Implemented recursive character text splitting (size: 500, overlap: 50) to preserve context.
- **Embedding Generation**: Used `sentence-transformers/all-MiniLM-L6-v2` (384d) to convert text chunks into dense vector representations.
- **Vector Store**: Built a FAISS (Facebook AI Similarity Search) index to enable fast and accurate semantic retrieval.

## Setup and Usage

### Prerequisites
- Python 3.10+
- Dependencies listed in `requirements.txt`

### Installation
```bash
pip install -r requirements.txt
```

### Running the Pipeline

**1. Data Preprocessing (Task 1)**
```bash
python src/data_preprocessing.py
python src/eda_analysis.py
```

**2. Vector Store Creation (Task 2)**
```bash
# Create stratified sample
python src/sampling.py

# Generate text chunks
python src/chunking.py

# Generate embeddings
python src/embedding.py

# Build FAISS vector store
python src/vector_store_builder.py
```

## Technologies Used
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **NLP & Embeddings**: Sentence-Transformers, LangChain
- **Vector Search**: FAISS
- **Interactive Analysis**: Jupyter Notebooks
