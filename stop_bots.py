import subprocess


def stop_bots():
    try:
        with open('api_keys.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("File api_keys.txt not found!")
        return

    for token in tokens:
        token = token.strip()
        if not token:
            print("Token cannot be empty!")
            continue

        safe_token = token.replace(':', '_')
        container_name = f"bot_{safe_token}"

        command = ['docker', 'stop', container_name]

        try:
            subprocess.run(command, check=True)
            print(f"Container {container_name} stopped.")
        except subprocess.CalledProcessError as e:
            print(f"Error stopping container {container_name}: {e}")


if __name__ == "__main__":
    stop_bots()
