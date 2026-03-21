import os
import json
import subprocess
import csv
from collections import Counter

PROCESSED_DIR = "data/processed" # folder that contains raw python code
OUTPUT_FILE = "data/metrics/dataset.csv"

# first run pylint to get results in json
def run_pylint(file_path):

    result = subprocess.run(
        ["pylint", file_path, "--output-format=json"],
        capture_output=True,
        text=True   # convert to string since pylint default output is in raw bytes
    )

    try:
        issues = json.loads(result.stdout)
    except json.JSONDecodeError:
        issues = []

    return issues

# function to summarize the pylint metrics
def summarize_pylint(issues):
    counts = Counter(issue["type"] for issue in issues)

    return {
        "pylint_errors": counts.get("error", 0),
        "pylint_warnings": counts.get("warning", 0),
        "pylint_refactor": counts.get("refactor", 0),
        "pylint_convention": counts.get("convention", 0),
        "pylint_total": len(issues)
    }

# quick example test
if __name__=="__main__":
    file_path = "data/processed/chatgpt/binary_search_run1.py"
    issues = run_pylint(file_path)
    # summary = summarize_pylint(issues)
    # print(summary)
    print(issues)
