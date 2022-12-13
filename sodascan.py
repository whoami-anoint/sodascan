import shodan

# Replace with your Shodan API key
API_KEY = "YOUR_API_KEY"

# Create a Shodan client
client = shodan.Shodan(API_KEY)

# Replace with the URL of the website you want to scan
url = "https://www.example.com"

# Perform the scan using the Shodan "scan" method
try:
    scan = client.scan(url)

    # Print the scan results
    print(scan)
except shodan.APIError as e:
    print(f"Error: {e}")
