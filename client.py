import requests
from register_user import register_user
from fetch_polls import fetch_polls
from poll_client import cast_vote, get_poll_results

if __name__ == "__main__":
    # --- Example for register_user ---
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

    # --- Example for fetch_polls ---
    print("\nAttempting to fetch polls with skip=0, limit=5")
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

    # --- Example for casting a vote and getting poll results (requires a valid token, poll_id, and option_id) ---
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