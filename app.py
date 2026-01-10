import gradio as gr
from src.rag.pipeline import RAGSystem
import os
import json
from datetime import datetime

# Initialize RAG System
vector_store_path = "vector_store/faiss_index"

# Check if vector store exists
if not os.path.exists(vector_store_path):
    raise FileNotFoundError(
        f"Vector store not found at {vector_store_path}. "
        "Please run the Task 2 notebook to create the vector store first."
    )

print("Initializing RAG System...")
rag_system = RAGSystem(vector_store_path)
print("RAG System ready!")

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

def log_interaction(query, response):
    """Log user interactions for analysis."""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "answer": response['answer'],
        "sources": [s.get('complaint_id', 'N/A') for s in response['context'][:3]]
    }
    with open("logs/chat_interactions.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def chat_interface(message, history):
    """
    Process user message and return response with sources.
    
    Args:
        message: User's question
        history: Chat history (list of [user_msg, bot_msg])
    
    Returns:
        Formatted response with answer and sources
    """
    if not message or message.strip() == "":
        return "Please enter a question."
    
    try:
        # Query RAG system
        response = rag_system.query(message)
        
        # Log the interaction
        log_interaction(message, response)
        
        # Format response with sources
        answer = response['answer']
        sources = response['context'][:3]  # Top 3 sources
        
        # Build formatted response
        formatted_response = f"{answer}\n\n**📚 Sources:**\n"
        for i, src in enumerate(sources, 1):
            company = src.get('company', 'Unknown')
            product = src.get('product', 'N/A')
            text_preview = src.get('text', '')[:150]
            formatted_response += f"\n{i}. **{company}** - {product}\n"
            formatted_response += f"   _{text_preview}..._\n"
        
        return formatted_response
    
    except Exception as e:
        return f"❌ Error processing your query: {str(e)}\n\nPlease try again or rephrase your question."

# Create Gradio Interface
demo = gr.ChatInterface(
    fn=chat_interface,
    title="💬 CrediTrust Complaint Analysis Assistant",
    description="""
    Ask questions about consumer complaints related to:
    - 💳 Credit cards
    - 💰 Personal loans
    - 🏦 Savings accounts
    - 💸 Money transfers
    
    This AI assistant uses a RAG (Retrieval-Augmented Generation) system to provide answers based on real consumer complaints from the CFPB database.
    """,
    examples=[
        "Why was my loan denied?",
        "How do I dispute a charge on my credit card?",
        "What are common issues with savings accounts?",
        "How long does a money transfer take?",
        "What should I do if my credit card was charged incorrectly?",
        "Why is my savings account showing unexpected fees?"
    ]
)

if __name__ == "__main__":
    demo.launch(
        share=False, 
        server_name="0.0.0.0", 
        server_port=7860,
        show_error=True
    )
