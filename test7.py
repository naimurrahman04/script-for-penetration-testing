import subprocess
import win32gui
import win32process

# Replace "executable.exe" with the path to your executable file
command = ["test7.exe"]

# Start the process and get its PID
process = subprocess.Popen(command, shell=True)
pid = process.pid

# Find the process's main window and hide it
hwnd = win32process.GetWindowThreadProcessId(pid)[0]
win32gui.ShowWindow(hwnd, 0)
