import os
import json

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"


def extract_code(filepath, output_dir):
    """
    Extract python code from a raw json and save as .py in data/processed
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    code = data["response"].strip() # remove leading / trailing whitespaces

    filename = os.path.basename(filepath) # e.g Path: data/raw/chatgpt/palindrome_check.json -> filename: 'palindrome_check.json'
    base_name = os.path.splitext(filename)[0] # splits the name from the extension into tuple -> ('palindrome_check', '.json')
    output_file = base_name + ".py" # becomes 'palindrome_check.py'
    output_path = os.path.join(output_dir, output_file) # e.g 'data/processed/chatgpt/palindrome_check.py'

    os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"saved {output_path}")


def process_all_models():
 # loop through all model folders in data/raw
    for model_folder in os.listdir(RAW_DIR):
        raw_dir = os.path.join(RAW_DIR, model_folder)
        processed_dir = os.path.join(PROCESSED_DIR, model_folder)

        if os.path.isdir(raw_dir):
            for filename in os.listdir(raw_dir):
                if filename.endswith(".json"):
                    filepath = os.path.join(raw_dir, filename)
                    extract_code(filepath, processed_dir)


if __name__ == "__main__":
    process_all_models()