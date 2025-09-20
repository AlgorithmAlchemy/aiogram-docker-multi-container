import subprocess

def run_bots():
    # Read tokens from file
    try:
        with open('api_keys.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("File api_keys.txt not found!")
        return

    # Start container for each token
    for token in tokens:
        if not token:
            print("Token cannot be empty!")
            return

        token = token.strip()  # Remove spaces and newlines
        if token:  # Check that the string is not empty
            # Replace colon with underscore
            safe_token = token.replace(':', '_')
            container_name = f"bot_{safe_token}"
            # Form command to start container
            command = [
                'docker', 'run', '-d', '--name', container_name,
                '--rm', 'aiogram_bot_image', 'python', 'main.py', token.strip()
            ]

            try:
                # Execute command
                subprocess.run(command, check=True)
                print(f"Container started: {container_name}")
            except subprocess.CalledProcessError as e:
                print(f"Error starting container {container_name}: {e}")

if __name__ == "__main__":
    run_bots()