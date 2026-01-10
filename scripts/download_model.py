from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import sys

def download_model():
    model_name = "google/flan-t5-small"
    print(f"Starting download for {model_name}...")
    try:
        # Download tokenizer
        print("Downloading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Download model
        print("Downloading model (approx 300MB)...")
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        print("Successfully downloaded and cached the model.")
        return True
    except Exception as e:
        print(f"Error downloading model: {e}")
        return False

if __name__ == "__main__":
    if download_model():
        sys.exit(0)
    else:
        sys.exit(1)
