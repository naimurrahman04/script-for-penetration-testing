import subprocess

# Read IP addresses from a text file
with open('ip.txt', 'r') as file:
    ip_list = file.read().splitlines()

for ip in ip_list:
    filename = f'{ip}.html'

    # Check if the file already exists
    try:
        with open(filename, 'x') as file:
            pass
    except FileExistsError:
        print(f"Skipping {ip}. File {filename} already exists.")
        continue

    # Run Nmap scan
    nmap_output = subprocess.check_output(['nmap', '-sS', '-A', '-T4', '-p-', ip])

    # Save raw Nmap output to HTML file
    raw_filename = f'{ip}_raw.html'
    with open(raw_filename, 'w') as raw_file:
        raw_file.write(nmap_output.decode())

    # Parse Nmap output
    open_ports = []
    closed_ports = []
    for line in nmap_output.decode().split('\n'):
        if 'open' in line and 'tcp' in line:
            port = line.split()[0]
            service = line.split()[2]
            open_ports.append((port, service))
        elif 'closed' in line and 'tcp' in line:
            port = line.split()[0]
            closed_ports.append(port)

    # Generate HTML report
    with open(filename, 'w') as file:
        file.write('<html>\n')
        file.write('<head>\n')
        file.write(f'<title>Nmap Scan Results for {ip}</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write(f'<h1>Nmap Scan Results for {ip}</h1>\n')

        # Add link to raw Nmap output
        file.write(f'<a href="{raw_filename}">Raw Nmap output</a>\n')

        # Add table of open and closed ports
        file.write('<table>\n')
        file.write('<tr><th>Port</th><th>State</th><th>Service</th></tr>\n')

        for port, service in open_ports:
            file.write(f'<tr><td>{port}</td><td>open</td><td>{service}</td></tr>\n')

        for port in closed_ports:
            file.write(f'<tr><td>{port}</td><td>closed</td><td>N/A</td></tr>\n')

        file.write('</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')

        print(f"Report generated for {ip}.")
