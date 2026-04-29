from pathlib import Path

ROOT = Path(__file__).parent
TASKS_FILE = ROOT / "tasks" / "tasks.json"
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
METRICS_DIR = ROOT / "data" / "metrics"
DATASET_FILE = METRICS_DIR / "dataset.csv"
