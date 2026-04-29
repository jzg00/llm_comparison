from pathlib import Path
import pandas as pd
from config import PROCESSED_DIR, DATASET_FILE
from utils import get_logger
from metrics.code_metrics import compute_loc
from metrics.run_pylint import run_pylint, summarize_pylint

logger = get_logger(__name__)


def extract_metadata(file_path: Path) -> dict:
    model = file_path.parent.name
    stem = file_path.stem  # e.g., "binary_search_run1"
    task, _, run = stem.rpartition("_run")
    return {"model": model, "task": task, "run": run}


def get_metrics(file_path: Path) -> dict:
    metrics = {}
    metrics.update(compute_loc(file_path))
    issues = run_pylint(file_path)
    metrics.update(summarize_pylint(issues))
    return metrics


def build_dataset() -> None:
    rows = []

    for py_file in PROCESSED_DIR.glob("*/*.py"):
        metadata = extract_metadata(py_file)
        metrics = get_metrics(py_file)
        rows.append(metadata | metrics)

    if not rows:
        logger.warning("No processed files found — dataset not written")
        return

    DATASET_FILE.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(DATASET_FILE, index=False)
    logger.info("Dataset written to %s (%d rows)", DATASET_FILE, len(df))


if __name__ == "__main__":
    build_dataset()
