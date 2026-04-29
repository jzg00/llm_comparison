import json
from pathlib import Path
from config import RAW_DIR, PROCESSED_DIR
from utils import get_logger

logger = get_logger(__name__)


def extract_code(filepath: Path, output_dir: Path) -> None:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    code = data["response"].strip()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filepath.with_suffix(".py").name

    output_path.write_text(code, encoding="utf-8")
    logger.info("Extracted %s", output_path)


def process_all_models() -> None:
    for model_dir in RAW_DIR.iterdir():
        if not model_dir.is_dir():
            continue
        processed_dir = PROCESSED_DIR / model_dir.name
        for json_file in model_dir.glob("*.json"):
            extract_code(json_file, processed_dir)


if __name__ == "__main__":
    process_all_models()
