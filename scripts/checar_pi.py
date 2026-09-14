import paramiko

# Variables to be filled in by the user
RASPBERRY_PI_IP = ""
RASPBERRY_PI_USER = ""
RASPBERRY_PI_PASSWORD = ""

def check_docker_containers():
    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()
    
    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the Raspberry Pi
        ssh_client.connect(hostname=RASPBERRY_PI_IP, username=RASPBERRY_PI_USER, password=RASPBERRY_PI_PASSWORD)
        
        # Execute the 'docker ps' command
        stdin, stdout, stderr = ssh_client.exec_command('docker ps')
        
        # Read the output and print it
        output = stdout.read().decode()
        print("Running Docker Containers:")
        print(output)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the SSH connection
        ssh_client.close()

if __name__ == '__main__':
    check_docker_containers()
