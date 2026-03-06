import requests
import csv
import json

# --- Configuration ---
API_URL = "https://jsonplaceholder.typicode.com/users"  # Replace with your API endpoint
HEADERS = {
    # "Authorization": "Bearer YOUR_API_KEY",  # Uncomment and add your key if needed
    "Accept": "application/json"
}
OUTPUT_FILE = "data.csv"

def fetch_data(url: str, headers: dict) -> list:
    """Fetch data from the API and return as a list of records."""
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    data = response.json()

    # If the API returns a dict with a nested list, unwrap it here.
    # e.g. if data = {"results": [...]}, use: return data["results"]
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        # Try common wrapper keys
        for key in ("results", "data", "items", "records"):
            if key in data and isinstance(data[key], list):
                return data[key]
        # Fall back to wrapping the dict itself
        return [data]
    return []

def save_to_csv(records: list, filepath: str) -> None:
    """Save a list of dicts to a CSV file."""
    if not records:
        print("No data to save.")
        return

    # Flatten nested dicts one level deep so they can be written to CSV
    flat_records = []
    for record in records:
        flat = {}
        for key, value in record.items():
            if isinstance(value, (dict, list)):
                flat[key] = json.dumps(value)  # Serialize nested structures
            else:
                flat[key] = value
        flat_records.append(flat)

    fieldnames = list(flat_records[0].keys())

    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flat_records)

    print(f"Saved {len(flat_records)} records to '{filepath}'.")

def main():
    print(f"Fetching data from: {API_URL}")
    records = fetch_data(API_URL, HEADERS)
    print(f"Fetched {len(records)} records.")
    save_to_csv(records, OUTPUT_FILE)

if __name__ == "__main__":
    main()
