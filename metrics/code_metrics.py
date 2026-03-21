def compute_loc(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    return {
        "loc": len(lines)
    }

