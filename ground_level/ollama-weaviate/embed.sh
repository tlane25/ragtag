#! /bin/bash

curl http://localhost:11434/api/embeddings -d '{ "model": "all-minilm", "prompt": "The sky is blue because of Rayleigh scattering"}'

# return is {"embedding":[ 0.26307252032398283, ...]} (many +ve and -ve elements in the array)
