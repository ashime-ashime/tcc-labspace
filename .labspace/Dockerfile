# Use a base image that already has Java and Maven
FROM maven:3.9-openjdk-11-slim

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for python
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# Copy lab content
COPY labspace-exercises/ /app/labspace-exercises/
COPY labspace.yaml /app/
COPY README.md /app/

# Set working directory
WORKDIR /app

# Install Python dependencies for the lab
RUN pip install --no-cache-dir \
    pytest \
    psycopg2-binary \
    testcontainers[postgres]

# Expose port for lab interface
EXPOSE 8080

# Default command - start a shell for interactive lab
CMD ["/bin/bash"]
