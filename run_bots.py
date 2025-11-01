import subprocess


def run_bots():
    try:
        with open('api_keys.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("File api_keys.txt not found!")
        return

    for token in tokens:
        if not token:
            print("Token cannot be empty!")
            return

        token = token.strip()
        if token:
            safe_token = token.replace(':', '_')
            container_name = f"bot_{safe_token}"
            command = [
                'docker', 'run', '-d', '--name', container_name,
                '--rm', 'aiogram_bot_image', 'python', 'main.py', token.strip()
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Container started: {container_name}")
            except subprocess.CalledProcessError as e:
                print(f"Error starting container {container_name}: {e}")


if __name__ == "__main__":
    run_bots()