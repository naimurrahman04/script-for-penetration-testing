import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init()

# Open the file containing the list of IP addresses
with open('ip.txt', 'r') as f:
    # Read the IP addresses into a list
    ips = f.readlines()

# Open a file to write the live hosts
with open('live.txt', 'w') as live_file:
    # Ping each IP address and print the ones that respond
    for ip in ips:
        ip = ip.strip()  # Remove any whitespace or newline characters
        res = subprocess.call(['ping', '-c', '1', ip])  # Ping the IP address
        if res == 0:
            print(Fore.GREEN + f'{ip} is live' + Style.RESET_ALL)
            live_file.write(ip + '\n')  # Write the live host to the file
        else:
            print(Fore.RED + f'{ip} is not live' + Style.RESET_ALL)
