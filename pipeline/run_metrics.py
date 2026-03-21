import os
import pandas as pd
from metrics.code_metrics import *
from metrics.run_pylint import run_pylint, summarize_pylint

PROCESSED_DIR = "data/processed"
OUTPUT_FILE = "data/metrics/dataset.csv"

# function to get metrics into a single dictionary
def get_metrics(file_path) -> dict:
    metrics = {}

    metrics.update(compute_loc(file_path)) # update() merges keys into the same dictionary

    issues = run_pylint(file_path)
    metrics.update(summarize_pylint(issues))

    return metrics

# function to get metadate
def extract_metadata():
    pass

# function to build dataset
def main():
    pass