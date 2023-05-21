import socket
import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init()

def is_port_open(ip, port):
    # Create a TCP socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout of 1 second

    # Attempt to connect to the specified port
    result = sock.connect_ex((ip, port))
    
    # Close the socket
    sock.close()

    # Return True if the port is open, False otherwise
    return result == 0

# Open the file containing the list of IP addresses
with open('ip.txt', 'r') as f:
    # Read the IP addresses into a list
    ips = f.readlines()

# Iterate over each IP address in the list
for ip in ips:
    ip = ip.strip()  # Remove any whitespace or newline characters

    # Ping the IP address
    res = subprocess.call(['ping', '-c', '1', ip])
    if res == 0:
        print(Fore.GREEN + f'{ip} is live' + Style.RESET_ALL)

        # Scan all ports for the IP address
        for port in range(1, 65536):
            if is_port_open(ip, port):
                print(Fore.YELLOW + f'Port {port} is open' + Style.RESET_ALL)
    else:
        print(Fore.RED + f'{ip} is not live' + Style.RESET_ALL)
