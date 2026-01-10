#!/usr/bin/env python3
"""
Quick test script to verify the RAG system is working correctly
before launching the full Gradio interface.
"""

from src.rag.pipeline import RAGSystem
import os

def test_rag_system():
    """Test the RAG system with a sample query."""
    
    vector_store_path = "vector_store/faiss_index"
    
    # Check if vector store exists
    if not os.path.exists(vector_store_path):
        print(f"❌ Error: Vector store not found at {vector_store_path}")
        print("Please run the Task 2 notebook to create the vector store first.")
        return False
    
    print("🔄 Initializing RAG System...")
    try:
        rag_system = RAGSystem(vector_store_path)
        print("✅ RAG System initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing RAG system: {e}")
        return False
    
    # Test query
    test_query = "Why was my loan denied?"
    print(f"\n📝 Test Query: {test_query}")
    print("🔄 Processing...")
    
    try:
        response = rag_system.query(test_query)
        
        print("\n✅ Response generated successfully!")
        print(f"\n💬 Answer:\n{response['answer']}")
        print(f"\n📚 Number of sources retrieved: {len(response['context'])}")
        
        print("\n📄 Top 3 Sources:")
        for i, src in enumerate(response['context'][:3], 1):
            company = src.get('company', 'Unknown')
            product = src.get('product', 'N/A')
            text_preview = src.get('text', '')[:100]
            print(f"\n{i}. {company} - {product}")
            print(f"   Preview: {text_preview}...")
        
        print("\n✅ All tests passed! The app is ready to launch.")
        return True
        
    except Exception as e:
        print(f"\n❌ Error during query: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_rag_system()
    exit(0 if success else 1)
