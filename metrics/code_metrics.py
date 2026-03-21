def compute_loc(file_path) -> dict:
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    # returning a dictionary here for easier assembly of dataset
    return {
        "loc": len(lines)
    }

# quick test
# if __name__=="__main__":
#     file_path = "data/processed/claude/rest_api_endpoint_run1.py"
#     loc = compute_loc(file_path)
#     print(loc)