# Pre-Configured TCC LabSpace Dockerfile
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    vim \
    nano \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic links for python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Python packages for TCC exercises
RUN pip3 install --no-cache-dir \
    testcontainers \
    psycopg2-binary \
    pytest \
    requests

# Copy lab content
COPY . /workspace/
WORKDIR /workspace

# Create directories for TCC simulation
RUN mkdir -p /workspace/.testcontainers \
    && mkdir -p /workspace/.testcontainers-desktop

# Start bash directly - no hanging issues
CMD ["/bin/bash"]