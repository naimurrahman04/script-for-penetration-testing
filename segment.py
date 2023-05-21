import socket
import subprocess
import time
from tqdm import tqdm
from docx import Document
from docx.shared import Inches
from builtins import FileNotFoundError
from builtins import ImportError

print("\033[1;36;40m EIC SEGMENTATION TEST \033[0m")

# Get local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip_address = s.getsockname()[0]
s.close()

# Define input and output file paths
input_file_path = "input.txt"
output_file_path = "output.docx"

# Read IP addresses from input file
with open(input_file_path, "r") as input_file:
    ip_addresses = input_file.read().splitlines()

# Create Word document and add a table
document = Document()
table = document.add_table(rows=1, cols=3)
table.style = "Table Grid"

# Add table headers
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Local IP address"
hdr_cells[1].text = "IP address"
hdr_cells[2].text = "Compliant"

# Ping each IP address and write results to table
for ip in tqdm(ip_addresses, desc="Pinging", ascii=True, unit="IP"):
    ping_result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.PIPE)
    compliant = "non-compliant" if ping_result.returncode == 0 else "compliant"
    row_cells = table.add_row().cells
    row_cells[0].text = local_ip_address
    row_cells[1].text = ip
    row_cells[2].text = compliant
    
    time.sleep(0.5)  # Wait for half a second before pinging the next IP address

# Save Word document
document.save(output_file_path)

print(f"Results saved to {output_file_path}")
