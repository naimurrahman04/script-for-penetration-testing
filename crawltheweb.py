import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


url = input("Enter the URL to crawl: ")
response = requests.get(url)

# Check if any security headers are present in the response headers
security_headers = {'Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection'}
found_headers = set()
for header in response.headers:
    if header in security_headers:
        found_headers.add(header)

output = "-" * 50 + "\n"
output += "Security Headers\n"
output += "-" * 50 + "\n"
if found_headers:
    output += f"Found security headers: {', '.join(found_headers)}\n"
else:
    output += "No security headers found.\n"
    
not_found_headers = security_headers - found_headers
if not_found_headers:
    output += f"Missing security headers: {', '.join(not_found_headers)}\n"
else:
    output += "All expected security headers are present.\n"
output += "-" * 50 + "\n"

soup = BeautifulSoup(response.content, 'html.parser')

# Find all URLs in the HTML and save them to a text file
urls_output = ""
urls = set()
for link in soup.find_all('a'):
    url = link.get('href')
    if url and not url.startswith('#'):
        urls.add(url)
for url in urls:
    urls_output += url + '\n'
output += f"{len(urls)} URLs found and saved to urls.txt\n"

# Find all links in the HTML forms and save them to a separate text file
form_links_output = ""
links = set()
forms = soup.find_all('form')
if forms:
    for form in forms:
        for link in form.find_all('a', href=True):
            url = link.get('href')
            if url:
                links.add(url)
    for link in links:
        form_links_output += link + '\n'
    output += f"{len(links)} form links found and saved to form_links.txt\n"
else:
    output += "No forms found.\n"
output += "-" * 50 + "\n"

# Combine all output into one variable
all_output = output + urls_output + form_links_output

# Print the output
print(all_output)
