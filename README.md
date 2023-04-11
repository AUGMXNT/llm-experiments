# llm-experiments

This is a dockerized environment for running LLM experiments w/ the OpenAI API and locally w/ an Nvidia CUDA GPU.
It mounts a single GPU and the following folders:
* `/data/docker/llm-experiments`
* `/data/ai/models`

## Prerequisites
* Docker and Docker Compose

## Installation
Setup:
```
git clone https://github.com/lhl/llm-experiments.git
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
