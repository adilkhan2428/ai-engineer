import requests 
import json

def fetch_and_save_api_data(api_url, filename):
    """Fetches JSON data from an external API, Handles network/file errors, and the cleaned data locally."""
    print("Connecting to API endpoint..")
    try:
        # 1. HTTP request with a timout safety net
        response = requests.get(api_url, timeout=5)

        # If the server return a 404 or 500 error, raise an exception automatically
        response.raise_for_status()

        # 2. Parse the incoming JSON response into a Python dict/list
        api_data = response.json() 

        # 3. Save the parsed data using File I/O and our JSON tool
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(api_data, f, indent=4)

        print(f"Success! Data fetched and saved successfully!")
    except requests.exceptions.RequestException as net_err:
        # cath every type error related to network or request/response
        print(f"API Network Error: {net_err}")
    except IOError as io_err:
        # Catches disk or permission errors when writing the file
        print(f"File I/O Error: {io_err}")

# Test the full pipeline using free mock API

fetch_and_save_api_data(api_url="https://jsonplaceholder.typicode.com/users/1",filename="files_save_test/customer_profile.json")