import requests
import csv

# Replace this URL with the API endpoint you want to fetch data from
api_url = "https://api.example.com/data"

try:
    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()  # Raises an error for bad responses
    data = response.json()  # Assuming the response is JSON

    # Check if data is a list of dictionaries
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        # Get CSV headers from the keys of the first dictionary
        headers = data[0].keys()

        # Write data to CSV
        with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print("Data successfully saved to data.csv")
    else:
        print("Unexpected data format. Expected a list of dictionaries.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
