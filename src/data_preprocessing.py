import pandas as pd
import os

RAW_DATA_PATH = 'prod/data/raw/complaints.csv'
PROCESSED_DATA_PATH = 'data/processed/filtered_complaints.csv'
CHUNK_SIZE = 10000

TARGET_PRODUCTS = {
    "Credit card",
    "Personal loan",
    "Savings account",
    "Money transfers"
}

# The dataset might use slightly different naming conventions or sub-products.
# We'll filter strictly first, based on user instructions.

def clean_narrative(text):
    if not isinstance(text, str):
        return ""
    # Basic cleaning: lowercase and strip whitespace
    return text.lower().strip()

def process_data():
    if not os.path.exists(RAW_DATA_PATH):
        print(f"File not found: {RAW_DATA_PATH}")
        return

    print(f"Processing {RAW_DATA_PATH} in chunks of {CHUNK_SIZE}...")
    
    # Initialize output file
    first_chunk = True
    total_processed = 0
    total_saved = 0

    # Ensure output directory exists
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)

    for chunk in pd.read_csv(RAW_DATA_PATH, chunksize=CHUNK_SIZE, low_memory=False):
        total_processed += len(chunk)
        
        # Filter for products
        # Using string matching to be robust
        mask_product = chunk['Product'].isin(TARGET_PRODUCTS)
        
        # Also filter for existing narratives
        mask_narrative = chunk['Consumer complaint narrative'].notna() & (chunk['Consumer complaint narrative'] != "")
        
        df_filtered = chunk[mask_product & mask_narrative].copy()
        
        if df_filtered.empty:
            continue

        # Clean narratives
        df_filtered['cleaned_narrative'] = df_filtered['Consumer complaint narrative'].apply(clean_narrative)
        
        # Save to CSV
        mode = 'w' if first_chunk else 'a'
        header = first_chunk
        df_filtered.to_csv(PROCESSED_DATA_PATH, mode=mode, header=header, index=False)
        
        first_chunk = False
        total_saved += len(df_filtered)
        
        print(f"Processed {total_processed} rows... Saved {total_saved} relevant complaints.", end='\r')

    print(f"\nCompleted. Total saved: {total_saved}")

if __name__ == "__main__":
    process_data()
