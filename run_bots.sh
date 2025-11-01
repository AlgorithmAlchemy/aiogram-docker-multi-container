#!/bin/bash

# Read the tokens from the file and run a container for each token
while IFS= read -r token; do
    docker run -d --name "bot_$token" --rm your_docker_image_name "$token"
done < api_keys.txt