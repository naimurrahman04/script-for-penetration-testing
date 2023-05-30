import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init()

# Open the file containing the list of IP addresses
with open('ip.txt', 'r') as f:
    # Read the IP addresses into a list
    ips = f.readlines()

# Ping each IP address and print the ones that respond
for ip in ips:
    ip = ip.strip()  # Remove any whitespace or newline characters
    res = subprocess.call(['ping', '-c', '1', ip])  # Ping the IP address
    if res == 0:
        print(Fore.GREEN + f'{ip} is live' + Style.RESET_ALL)
    else:
        print(Fore.RED + f'{ip} is not live' + Style.RESET_ALL)
