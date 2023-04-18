# llm-experiments

This is a dockerized environment for running LLM experiments w/ the OpenAI API and locally w/ an Nvidia CUDA GPU.
It mounts a single GPU and the following folders:
* `/data/docker/llm-experiments`
* `/data/ai/models`

See this related LLM Experiments worksheet for related data: https://docs.google.com/spreadsheets/d/1kT4or6b0Fedd-W_jMwYpb63e1ZR3aePczz3zlbJW-Y4/edit#gid=741531996
* List of accessible foundational models
* List of fine-tunes
* List of Datasets
* `lm-eval` results
* Some ChatGPT bencmark tests

Also, here are some other prior work:
* [Practical LLMs](https://mostlyobvious.org/?link=/Reference%2FSoftware%2FGenerative%20AI%2FPractical%20LLMs) - results from poking around w/ self-hosted LLMs
* [AI Safety](https://mostlyobvious.org/?link=/Reference%2FSoftware%2FGenerative%20AI%2FSafety) - my research on AI Ethics and Safety (including AGI xrisk)

## Prerequisites
* Docker and Docker Compose

## Installation
Setup:
```
git clone https://github.com/AUGMXNT/llm-experiments.git
cd llm-experiments

# Modify the volume paths, UID/GUIDs in the Dockerfile and docker-compose.yml 

docker-compose build
```

# Setup
```
cp env.sample .env
# and update w/ your keys

```

# Run
```
# This script finds the instance and runs `docker-compose up -d` if necessary
./connect_docker_instance.sh
```

You should now be inside the Docker container with access to your mounted directories, necessary tools, and environment variables. `conda` and `mamba` are pre-installed and you should be in the `(base)` venv.

We do this on the initial build, but to run the code, you'll probably want to run as necessary:
```
pip install -r requirements.txt
```

If you make any changes to the `Dockerfile` or `docker-compose.yml`, you can update the Docker image by running:
```
docker-compose build
docker-compose up -d
```
