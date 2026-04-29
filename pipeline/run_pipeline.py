from pipeline.generate_response import generate_response
from pipeline.extract_code import process_all_models
from pipeline.run_metrics import build_dataset
from utils import get_logger

logger = get_logger(__name__)


def main_pipeline():
    logger.info("Starting pipeline")
    generate_response()
    process_all_models()
    build_dataset()
    logger.info("Pipeline complete")


if __name__ == "__main__":
    main_pipeline()
