import requests
import webbrowser
import socket
import nmap
from urllib.parse import urlparse
from pprint import pprint
from tqdm import tqdm
from colorama import Fore, Style
# Set the headers to be sent with the request


# Prompt the user to input the URL
url = input('Enter the URL: ')
domain = urlparse(url).netloc
print(domain)
ip=socket.gethostbyname(domain)
print(socket.gethostbyname(domain))
# Make a GET request to the specified URL with the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

with tqdm(total=100, desc='Loading') as pbar:
        response = requests.get(url, headers=headers)
for _ in range(100):
        pbar.update(1)
# Print the request header
print(Fore.BLUE + Style.BRIGHT+"request header")
pprint(response.request.headers)
print(Style.RESET_ALL)
# Print the response header
print(Fore.GREEN + Style.BRIGHT +"response header")
pprint(response.headers)
print(Style.RESET_ALL)
# Print the response content
pprint(response.content)

with open('temp01.html', 'w') as f:
    f.write(response.content.decode('utf-8'))

# Open the temporary HTML file in the default web browser
webbrowser.open('temp01.html')
pprint("testing http chunked")
payload = "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nPOST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 4\r\n\r\nabcd"


with tqdm(total=100, desc='Loading') as pbar:
# Send the HTTP request with the payload and headers
        response = requests.request(method='POST', url=url, headers=headers, data=payload)
for _ in range(100):
        pbar.update(1)

# Print the request header
print(Fore.BLUE + Style.BRIGHT+"request header")
pprint(response.request.headers)
print(Style.RESET_ALL)
# Print the response header
print(Fore.GREEN + Style.BRIGHT +"response header")
pprint(response.headers)
print(Style.RESET_ALL)
# Print the response content
pprint(response.content)

with open('temp02.html', 'w') as f:
    f.write(response.content.decode('utf-8'))

# Open the temporary HTML file in the default web browser
webbrowser.open('temp02.html')

scanner = nmap.PortScanner()

# Use the PortScanner object to scan the specified IP address
scanner.scan(ip, arguments='-p-')

# Loop through the open ports found by the PortScanner object
for host in scanner.all_hosts():
    print('Host : %s (%s)' % (host, scanner[host].hostname()))
    print('State : %s' % scanner[host].state())

    for proto in scanner[host].all_protocols():
        print('Protocol : %s' % proto)

        ports = scanner[host][proto].keys()
        sorted_ports = sorted(ports)

        for port in sorted_ports:
            print('Port : %s\tState : %s\tService : %s' % (port, scanner[host][proto][port]['state'], scanner[host][proto][port]['name']))
