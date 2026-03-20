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

# function to summarize the pylint results