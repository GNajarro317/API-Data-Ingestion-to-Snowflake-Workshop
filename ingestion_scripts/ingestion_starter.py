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
    # TODO: Load environment variables into system context
    pass

def fetch_api_data(base_url, endpoint):
    """
    Fetches JSON data from the specified API endpoint.
    
    Args:
        base_url (str): The root URL of the API.
        endpoint (str): The specific path to fetch (e.g., '/posts').
        
    Returns:
        dict/list: The parsed JSON data from the response, in the form of a python dict.
    """
    # TODO: Construct our target URL
    url = None

    print(f"\nFetching data from: {url}")
    
    # TODO: Send a GET request to the URL using requests
    # TODO: Check if response status code is 200 (OK)
    # TODO: Return parsed JSON data if successful, else print error and return None
    pass

def connect_to_snowflake():
    """
    Establishes a connection to the Snowflake database using environment variables.
    
    Returns:
        snowflake.connector.connection: The active connection object.
    """
    print("Connecting to Snowflake...")
    # TODO: Create and return a snowflake connection object using os.getenv() for credentials
    # Credentials needed: account, user, password, warehouse, database, schema
    pass

def load_data_to_snowflake(cursor, table_name, data):
    """
    Inserts the JSON data into the Snowflake table as a VARIANT type.
    
    Args:
        cursor: The active Snowflake cursor object.
        data (dict/list): The JSON data to insert.
    """
    # TODO: Write SQL INSERT query targeting table_name and RAW_PAYLOAD column
    # TODO: Convert Python object to JSON string using json.dumps()
    # TODO: Execute query using cursor.execute()
    pass

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
    
    # TODO: Call fetch_api_data() with api_base_url and endpoint
    data = None
    
    # 3. Database Operations
    # TODO: Establish connection using connect_to_snowflake()
    conn = None

    # TODO: Open a cursor from the connection
    cursor = None

    # TODO: Call load_data_to_snowflake() to insert the data

    
    # 4. Cleanup
    print("Pipeline complete!")
    # TODO: Close cursor and connection objects

if __name__ == "__main__":
    main()