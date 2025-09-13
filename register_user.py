import requests

def register_user(username, password):
    """
    Registers a new user via the /register endpoint.

    Args:
        username (str): The username for the new user.
        password (str): The password for the new user.

    Returns:
        dict: A dictionary containing the response from the API, or an error message.
    """
    url = "http://localhost:8000/register"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
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
    # You would typically get these from user input or a configuration
    test_username = "testuser"
    test_password = "testpassword"

    print(f"Attempting to register user: {test_username}")
    result = register_user(test_username, test_password)

    if "error" in result:
        print(f"Registration failed: {result['error']}")
        if "status_code" in result:
            print(f"Status Code: {result['status_code']}")
        if "response" in result:
            print(f"Response: {result['response']}")
    else:
        print("Registration successful!")
        print(result)