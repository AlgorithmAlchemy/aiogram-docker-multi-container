import subprocess


def stop_bots():
    # Read tokens from file
    try:
        with open('api_keys.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("File api_keys.txt not found!")
        return

    # Stop container for each token
    for token in tokens:
        token = token.strip()  # Remove spaces and newlines
        if not token:
            print("Token cannot be empty!")
            continue

        # Replace colon with underscore to match container names
        safe_token = token.replace(':', '_')
        container_name = f"bot_{safe_token}"

        # Form command to stop container
        command = ['docker', 'stop', container_name]

        try:
            # Stop container
            subprocess.run(command, check=True)
            print(f"Container {container_name} stopped.")
        except subprocess.CalledProcessError as e:
            print(f"Error stopping container {container_name}: {e}")


if __name__ == "__main__":
    stop_bots()