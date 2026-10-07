import os
import requests
import snowflake.connector
import json
from dotenv import load_dotenv

def load_environment():
    """
    Loads environment variables from the .env file.
    """
    print("Loading environment variables...")
    load_dotenv()

def fetch_api_data(base_url, endpoint):
    """Fetches JSON data from the specified API endpoint."""
    url = base_url + endpoint

    print(f"\nFetching data from: {url}")

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve {endpoint}. Status code: {response.status_code}")
        return None

def connect_to_snowflake():
    """Establishes a connection to the Snowflake database."""
    print("Connecting to Snowflake...")
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse="WORKSHOP_WH",
        database="WORKSHOP_DB",
        schema="RAW"
    )

def load_data_to_snowflake(cursor, table_name, data):
    """Inserts the JSON data into the Snowflake table as a VARIANT type."""
    query = f"INSERT INTO {table_name} (RAW_PAYLOAD) SELECT PARSE_JSON(%s)"
    
    # We use json.dumps to convert the Python list/dict back into a raw JSON string for Snowflake
    cursor.execute(query, (json.dumps(data),))
    print(f"Successfully loaded data into '{table_name}'.")

def main():
    """
    The main orchestrator function that chains the steps together.
    """
    # 1. Setup Environment
    load_environment()
    
    # 2. Fetch Data
    api_base_url = "https://jsonplaceholder.typicode.com"
    endpoint = "/posts"
    target_table = "raw_posts"
    data = fetch_api_data(api_base_url, endpoint)
    
    # 3. Database Operations
    conn = connect_to_snowflake()
    cursor = conn.cursor()
    
    load_data_to_snowflake(cursor, target_table, data)
    
    # 4. Cleanup
    print("Pipeline complete!")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()