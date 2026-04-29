def compute_loc(file_path) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    non_blank = sum(1 for line in lines if line.strip())
    return {"loc": non_blank}