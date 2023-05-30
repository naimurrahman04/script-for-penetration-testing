import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

HEADERS_TO_CHECK = [    "Content-Security-Policy",    "Strict-Transport-Security",    "X-XSS-Protection",    "X-Content-Type-Options",    "Referrer-Policy",    "Feature-Policy",]

def check_headers(url):
    headers = {"Status Code": "Error"}
    try:
        response = requests.head(url)
        headers["Status Code"] = response.status_code
    except requests.exceptions.RequestException:
        pass
    for header in HEADERS_TO_CHECK:
        normalized_header = header.replace("-", " ").title().replace(" ", "-")
        if normalized_header in response.headers:
            headers[header] = response.headers[normalized_header]
        else:
            headers[header] = "Not found"
    return {url: headers}

website_url = "https://www.uttarabank-bd.com/"
response = requests.get(website_url)

soup = BeautifulSoup(response.text, "html.parser")

urls = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and href.startswith("http"):
        urls.append(href)

results = []
for url in urls:
    result = check_headers(url)
    results.append(result)

headers = ["URL", "Status Code", "Content-Security-Policy", "Strict-Transport-Security", "X-XSS-Protection", "X-Content-Type-Options", "Referrer-Policy", "Feature-Policy"]
table = []
for result in results:
    url = list(result.keys())[0]
    row = [url, result[url].pop("Status Code")]
    for header in headers[2:]:
        row.append(result[url][header])
    table.append(row)

print(tabulate(table, headers=headers))

