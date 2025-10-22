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

# Make scripts executable
RUN chmod +x /workspace/.labspace/lab-welcome.sh

# Start with lab welcome banner and interactive bash
CMD ["/bin/bash", "-c", "/workspace/.labspace/lab-welcome.sh && exec /bin/bash"]