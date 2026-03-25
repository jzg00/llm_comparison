# import main functions from pipeline
from pipeline.generate_response import generate_response
from pipeline.extract_code import process_all_models
from pipeline.run_metrics import build_dataset

def main_pipeline():
    print("Running pipeline...")
    
    generate_response()
    process_all_models()
    build_dataset()

    print("\nFinished")

if __name__=="__main__":
    main_pipeline()