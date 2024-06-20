#! /bin/bash

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec -it ollama ollama pull all-minilm
docker exec -it ollama sh
