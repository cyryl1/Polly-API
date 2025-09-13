import requests

def fetch_polls(skip: int = 0, limit: int = 10):
    """
    Fetches paginated poll data from the /polls endpoint.

    Args:
        skip (int): The number of items to skip.
        limit (int): The maximum number of items to return.

    Returns:
        dict: A dictionary containing the response from the API, or an error message.
    """
    base_url = "http://localhost:8000"
    endpoint = f"/polls?skip={skip}&limit={limit}"
    url = base_url + endpoint

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}", "status_code": response.status_code, "response": response.json()}
    except requests.exceptions.ConnectionError as conn_err:
        return {"error": f"Connection error occurred: {conn_err}"}
    except requests.exceptions.Timeout as timeout_err:
        return {"error": f"Timeout error occurred: {timeout_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"An unexpected error occurred: {req_err}"}

if __name__ == "__main__":
    # Example usage:
    print("Attempting to fetch polls with skip=0, limit=5")
    result = fetch_polls(skip=0, limit=5)

    if "error" in result:
        print(f"Failed to fetch polls: {result['error']}")
        if "status_code" in result:
            print(f"Status Code: {result['status_code']}")
        if "response" in result:
            print(f"Response: {result['response']}")
    else:
        print("Successfully fetched polls:")
        for poll in result:
            print(f"  - Poll ID: {poll.get('id')}, Question: {poll.get('question')}")

    print("\nAttempting to fetch polls with skip=5, limit=5")
    result = fetch_polls(skip=5, limit=5)

    if "error" in result:
        print(f"Failed to fetch polls: {result['error']}")
        if "status_code" in result:
            print(f"Status Code: {result['status_code']}")
        if "response" in result:
            print(f"Response: {result['response']}")
    else:
        print("Successfully fetched polls:")
        for poll in result:
            print(f"  - Poll ID: {poll.get('id')}, Question: {poll.get('question')}")