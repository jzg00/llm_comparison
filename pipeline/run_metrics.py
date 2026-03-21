import os
import pandas as pd
from metrics.code_metrics import *
from metrics.run_pylint import run_pylint, summarize_pylint

RAW_DIR = "data/raw"
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

    model = parts[2]
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
def main():
    pass