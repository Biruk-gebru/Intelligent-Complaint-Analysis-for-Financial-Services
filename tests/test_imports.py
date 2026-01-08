import sys
import os
import unittest

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestImports(unittest.TestCase):
    def test_imports(self):
        """Simple test to verify modules can be imported."""
        try:
            from src.chunking import create_text_chunks
            from src.embedding import generate_embeddings
            from src.vector_store_builder import FAISSVectorStore
            from src.rag.pipeline import RAGSystem
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Import failed: {e}")

if __name__ == '__main__':
    unittest.main()
