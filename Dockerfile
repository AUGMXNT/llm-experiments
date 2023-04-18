# Dockerfile

ARG TARGET_ARCH=x86_64
# ARG TARGET_ARCH=aarch64

# Use NVIDIA CUDA base image - 11.8 for less GPTQ-for-LLaMa drama
ARG UBUNTU_VERSION=20.04
ARG CUDA_VERSION=11.8.0
FROM nvidia/cuda:${CUDA_VERSION}-devel-ubuntu${UBUNTU_VERSION}

# Install system packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y alsa-utils build-essential byobu bzip2 espeak git locales neovim sudo wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Locale Setup
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Local user setup
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER=lhl
RUN groupadd -g ${GROUP_ID} $USER && \
    useradd -u ${USER_ID} -g ${GROUP_ID} -m -s /bin/bash $USER

# Grant passwordless sudo rights to the user '$USER'
RUN echo '$USER ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Switch to the '$USER' user
USER $USER

# Install Miniconda
ARG TARGET_ARCH
RUN if [ "$TARGET_ARCH" = "x86_64" ] ; then \
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh; \
    elif [ "$TARGET_ARCH" = "aarch64" ]; then \
        wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh -O ~/miniconda.sh; \
    else \
        echo "Unsupported architecture: $TARGET_ARCH"; \
        exit 1; \
    fi
RUN chmod +x ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p /home/$USER/miniconda && \
    rm ~/miniconda.sh

# Add conda to PATH
ENV PATH="/home/$USER/miniconda/bin:$PATH"
ENV CONDA_AUTO_ACTIVATE_BASE=true

# Install Mamba
RUN conda install -y -c conda-forge mamba

# Install Python 3.10, JupyterLab
RUN mamba install -y python=3.10
RUN mamba install -y -c conda-forge jupyterlab


# Make sure we start w/ conda active
RUN conda init

# Install Python packages from the requirements.txt
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Create a working directory
WORKDIR /data/docker/llm-experiments

# Mount the local path to the working directory
VOLUME ["/data/docker/llm-experiments", "/data/ai/models"]
