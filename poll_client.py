import requests

def cast_vote(poll_id: int, option_id: int, token: str):
    """
    Casts a vote on an existing poll.

    Args:
        poll_id (int): The ID of the poll to vote on.
        option_id (int): The ID of the option to vote for.
        token (str): The JWT token for authentication.

    Returns:
        dict: A dictionary containing the response from the API, or an error message.
    """
    url = f"http://localhost:8000/polls/{poll_id}/vote"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "option_id": option_id
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

def get_poll_results(poll_id: int):
    """
    Retrieves the results for a specific poll.

    Args:
        poll_id (int): The ID of the poll to retrieve results for.

    Returns:
        dict: A dictionary containing the poll results, or an error message.
    """
    url = f"http://localhost:8000/polls/{poll_id}/results"

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
    # Example usage for casting a vote (requires a valid token, poll_id, and option_id)
    # You would typically obtain these from a login process and poll listing
    test_poll_id = 1
    test_option_id = 1
    test_token = "YOUR_JWT_TOKEN_HERE" # Replace with a valid JWT token

    print(f"\nAttempting to cast vote for poll {test_poll_id}, option {test_option_id}")
    vote_result = cast_vote(test_poll_id, test_option_id, test_token)

    if "error" in vote_result:
        print(f"Failed to cast vote: {vote_result['error']}")
        if "status_code" in vote_result:
            print(f"Status Code: {vote_result['status_code']}")
        if "response" in vote_result:
            print(f"Response: {vote_result['response']}")
    else:
        print("Vote cast successfully!")
        print(vote_result)

    # Example usage for getting poll results
    print(f"\nAttempting to get results for poll {test_poll_id}")
    results = get_poll_results(test_poll_id)

    if "error" in results:
        print(f"Failed to get poll results: {results['error']}")
        if "status_code" in results:
            print(f"Status Code: {results['status_code']}")
        if "response" in results:
            print(f"Response: {results['response']}")
    else:
        print("Successfully retrieved poll results:")
        print(f"  Question: {results.get('question')}")
        for option_result in results.get('results', []):
            print(f"    - Option: {option_result.get('text')}, Votes: {option_result.get('vote_count')}")