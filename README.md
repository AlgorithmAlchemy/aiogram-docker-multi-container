# Aiogram Telegram Bot in Docker

## Description

This is an example of a bot built on the Aiogram library, packaged in a Docker container for easy deployment and management. The bot features both a regular button keyboard and inline buttons for user interaction. The main goal of the project is to enable running multiple bot instances with different tokens in separate containers for scalability and convenient management.

## Bot Features

- Regular button keyboards for text communication
- Inline buttons with callback responses
- Convenient bot management via Docker
- Support for multiple bots using separate containers for each token

## Requirements

- Python 3.7+
- Docker
- `api_keys.txt` file with bot tokens

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/your-repo/aiogram-docker-sample.git
   cd aiogram-docker-sample
   ```

2. **Create Docker image:**
Run the command to build the Docker image for the bot:
    ```
   docker build -t aiogram_bot_image .
    ```

## **Main Commands:**
#### Start all bots:
     python run_bots.py
   

#### Stop all bots:
      python stop_bots.py

#### Check active containers:
      docker ps

#### View container logs:
      docker logs <container_name>

#### Stop a specific container:
      docker stop <container_name>
