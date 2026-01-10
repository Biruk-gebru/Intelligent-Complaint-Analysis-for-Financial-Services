import sys
import os
import pandas as pd

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.rag.pipeline import RAGSystem

def main():
    print("Initializing RAG System...")
    vector_store_path = "vector_store/faiss_index"
    
    # Check if vector store exists
    if not os.path.exists(vector_store_path):
        print(f"Error: Vector store not found at {vector_store_path}")
        return

    try:
        rag_system = RAGSystem(vector_store_path)
    except Exception as e:
        print(f"Failed to initialize RAG System: {e}")
        return

    # Define Test Queries
    queries = [
        "Why was my loan denied?",
        "How to dispute a charge?",
        "What are the unauthorized transaction fees?",
        "My credit score dropped unexpectedly",
        "How long does a money transfer take?"
    ]

    # Run Evaluation
    results = []
    print("\nStarting Evaluation...")

    for q in queries:
        print(f"\nQuerying: {q}")
        try:
            response = rag_system.query(q)
            
            # Extract top snippet
            top_snippet = response['context'][0]['text'][:200] + "..." if response['context'] else "No context found"
            
            results.append({
                "Question": q,
                "Generated Answer": response['answer'].replace('\n', ' '), # Clean newlines for table
                "Retrieved Context (Snippet)": top_snippet.replace('\n', ' '),
                "Quality Score (1-5)": "3",  # Placeholder
                "Comments": "Auto-generated"
            })
            print(f"Answer: {response['answer']}")
        except Exception as e:
            print(f"Error processing query '{q}': {e}")
            results.append({
                "Question": q,
                "Generated Answer": f"Error: {e}",
                "Retrieved Context (Snippet)": "",
                "Quality Score (1-5)": "0",
                "Comments": "Failed"
            })

    df_results = pd.DataFrame(results)
    
    # Save Report
    report_path = "report/rag_evaluation.md"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    print(f"\nSaving report to {report_path}...")
    with open(report_path, "w") as f:
        f.write("# RAG Evaluation Report\n\n")
        f.write(df_results.to_markdown(index=False))
        
    print("Done.")

if __name__ == "__main__":
    main()
