import os
import pandas as pd
from metrics.code_metrics import compute_loc
from metrics.run_pylint import run_pylint, summarize_pylint

RAW_DIR = "data/raw" # use if metedata is extracted from raw JSON
PROCESSED_DIR = "data/processed"
OUTPUT_FILE = "data/metrics/dataset.csv"

# function to get metrics into a single dictionary
def get_metrics(file_path) -> dict:
    metrics = {}

    # code metrics
    metrics.update(compute_loc(file_path)) # update() merges keys into the same dictionary
    # pylint metrics
    issues = run_pylint(file_path)
    metrics.update(summarize_pylint(issues))

    return metrics

# function to get metadate
def extract_metadata(file_path):
    parts = file_path.split(os.sep)

    model = parts[1]
    filename = parts[-1]

    # consider changing to load metadata from raw JSON instead
    name_parts = filename.replace(".py", "").split("_")
    task = "_".join(name_parts[:-1])
    run = name_parts[-1]

    return {
        "model": model,
        "task": task,
        "run": run,
        "file_name": filename
    }


# function to build dataset
def build_dataset():
    # list of dictionaries (row-wise)
    rows = []

    # iterate through processed .py files for each model
    for model in os.listdir(PROCESSED_DIR):
        model_path = os.path.join(PROCESSED_DIR, model)
    
        for file in os.listdir(model_path):
            if not file.endswith(".py"):
                continue
        
        file_path = os.path.join(model_path, file)

        metadata = extract_metadata(file_path)

        metrics = get_metrics(file_path)

        row = metadata | metrics # merge dicts into one flat row
        rows.append(row)

    if rows:
        df = pd.DataFrame(rows)
        print(df) # quick test
    
if __name__=="__main__":
    build_dataset()